#include "Option.hpp"

Option::Option(const std::vector<int>& assetCurrencyMapping,
               const std::vector<InterestRateModel>& foreignInterestRates,
               const InterestRateModel& domesticInterestRate,
               TimeGrid* monitoringTimeGrid)
    : assetCurrencyMapping(assetCurrencyMapping),
      foreignInterestRates(foreignInterestRates),
      domesticInterestRate(domesticInterestRate),
      monitoringTimeGrid(monitoringTimeGrid) {}

Option::Option() {}

void Option::createPathsInLocalCurrency(PnlMat *path, PnlMat* newPath) const {
    PnlVect* dates = pnl_vect_copy(monitoringTimeGrid->dates);
    PnlVect* riskFreeAsset = pnl_vect_create(path->m);
    PnlVect* St = pnl_vect_create(path->m);
    PnlVect* Xt = pnl_vect_create(path->m);
    int assetsSize = 3;
    for (int i = assetsSize; i < path->n; i++) {
        pnl_mat_get_col(St, newPath, i);
        double interestRate = foreignInterestRates[i-assetsSize].interestRate;
        for (int j = 0; j < riskFreeAsset->size; j++) {
            LET(riskFreeAsset, j) = std::exp(-interestRate * (double)GET(dates, j)/252);
        }
        pnl_vect_mult_vect_term(St, riskFreeAsset);
        pnl_mat_set_col(newPath, St, i);
    }
    for (int i = 1; i < assetsSize; i++) {
        pnl_mat_get_col(St, newPath, i);
        pnl_mat_get_col(Xt, newPath, assetsSize+i-1);
        pnl_vect_div_vect_term(St, Xt);
        pnl_mat_set_col(newPath, St, i);
    }
}

PnlVect* Option::payoff(PnlMat *path, double time) const {
    PnlMat* newPath = pnl_mat_create(path->m, path->n);
    pnl_mat_clone(newPath, path);
    createPathsInLocalCurrency(path, newPath);
    int nbDates = newPath->m;   // Nombre de dates (T0, T1, ..., Tc)
    int nbIndices = 3; // Nombre d'indices (3 : Euro Stoxx 50, S&P 500, Hang Seng)
    int nbCol = newPath->n;
    // Prix initiaux à T0
    PnlVect *S0 = pnl_vect_create(nbCol);
    pnl_mat_get_row(S0, newPath, 0); // Récupérer les prix initiaux à T0

    double somme_des_perf = 0.0;
    double dividendeDiscounted = 0.0;
    PnlVect* dividendes = pnl_vect_create_from_zero(5);
    // Parcours des dates de T1 à Tc
    for (int t = 1; t < nbDates; t++) {
        PnlVect *St = pnl_vect_create(nbCol);
        pnl_mat_get_row(St, newPath, t); // Récupérer les prix aux dates T1, T2, ..., Tc

        // Calcul des performances des 3 indices
        PnlVect *performances = pnl_vect_create(nbIndices);
        for (int i = 0; i < nbIndices; i++) {
            LET(performances, i) = (GET(St, i) / GET(S0, i)) - 1.0; // (St / S0) - 1
        }

        // Meilleure performance limitée à 6%
        double maxPerf = pnl_vect_max(performances);
        maxPerf = std::min(maxPerf, 0.06); // Limite max à 6%

        // Ajustement selon les règles
        if (maxPerf < -0.2) {
            maxPerf = -0.2;
        } else if (maxPerf > -0.04) {
            maxPerf = std::max(0.0, maxPerf);
        }

        // Ajouter à la somme des performances annuelles
        somme_des_perf += maxPerf;
        // Calcul du portefeuille équipondéré des 2 indices les moins performants
        if (t < nbDates - 1) {
            // Seulement pour T1 à T4
            int minIdx1 = -1, minIdx2 = -1;
            double min1 = 1e9, min2 = 1e9;

            for (int i = 0; i < nbIndices; i++) {
                double perf = GET(performances, i);
                if (perf < min1) {
                    min2 = min1;
                    minIdx2 = minIdx1;
                    min1 = perf;
                    minIdx1 = i;
                } else if (perf < min2) {
                    min2 = perf;
                    minIdx2 = i;
                }
            }

            // Calcul du portefeuille équipondéré des 2 indices les moins performants
            double perf_portefeuille = (min1 + min2) / 2.0;
            if (perf_portefeuille > 0) {
                dividendeDiscounted += 25 * perf_portefeuille * domesticInterestRate.discount(time, GET(monitoringTimeGrid->dates, t)) ; // Ajout du dividende
                LET(dividendes, t-1) = 25 * perf_portefeuille * domesticInterestRate.discount(time, GET(monitoringTimeGrid->dates, t));
            }
        }
        pnl_vect_print(dividendes);
        pnl_vect_free(&St);
        pnl_vect_free(&performances);
    }

    // Calcul du paiement final
    double payoff = 0.0;
    if (somme_des_perf > 0) {
        payoff = valeurLiquidativeInitiale * (1 + somme_des_perf); // Augmentation de S0
    } else if (somme_des_perf > -0.2) {
        payoff = valeurLiquidativeInitiale; // Valeur initiale
    } else {
        payoff = valeurLiquidativeInitiale * std::max(1 - 0.4, 1 + somme_des_perf); // Limité à -40%
    }

    pnl_vect_free(&S0);
    double discountFactor = domesticInterestRate.discount(time, GET(monitoringTimeGrid->dates, nbDates - 1));
    LET(dividendes, 4) = payoff * discountFactor;
    return dividendes; // Ajout du dividende
}

void Option::updateOption(Parser* parser) {
    if (!foreignInterestRates.empty()) {
        foreignInterestRates.clear();
    }
    double domesticRate = GET(parser->interestRates, 0);
    domesticInterestRate = *new InterestRateModel(domesticRate);
    for (int i = 1; i <= parser->currenciesSize; i++) {
        double rate = GET(parser->interestRates, i);
        InterestRateModel interestRateModel(rate);
        foreignInterestRates.push_back(interestRateModel);
    }
    monitoringTimeGrid = parser->datesManager;
}