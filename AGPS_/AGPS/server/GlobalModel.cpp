#include "GlobalModel.hpp"
#include "pnl/pnl_vector.h"
#include "pnl/pnl_matrix.h"
#include "RiskyDynamics.hpp"

// Constructeur
GlobalModel::GlobalModel() {
    domesticInterestRate = *new InterestRateModel();
    monitoringTimeGrid = new TimeGrid();
}

GlobalModel::GlobalModel(
    const std::vector<RiskyAsset>& assets,
    const std::vector<Currency>& currencies,
    TimeGrid* monitoringTimeGrid,
    const InterestRateModel& domesticInterestRate
)
    : assets(assets),
      currencies(currencies),
      monitoringTimeGrid(monitoringTimeGrid),
      domesticInterestRate(domesticInterestRate) {}

// Destructeur
GlobalModel::~GlobalModel() {
    // Si nécessaire, libérer les ressources allouées dynamiquement (ici monitoringTimeGrid)
    // Par exemple, si monitoringTimeGrid a été alloué dynamiquement (via new), libérer la mémoire ici
    // delete monitoringTimeGrid; // si monitoringTimeGrid est alloué dynamiquement
}

void GlobalModel::updateGlobalModel(Parser* parser) {
    if (!assets.empty()) {
      assets.clear();
    }
    if (!currencies.empty()) {
      currencies.clear();
    }
    // Update Vector of Assets
    PnlVect* assetVolLine = pnl_vect_new();
    PnlVect* currencyVolLine = pnl_vect_new();
    for (int i = 0; i < parser->assetsSize; i++) {
        double rate = GET(parser->interestRates, i);
        InterestRateModel* interestRateModel = new InterestRateModel(rate);
        pnl_mat_get_row(assetVolLine, parser->choleskyMatrix, i);
        pnl_vect_mult_scalar(assetVolLine, GET(parser->volatilities, i));
        if (i != 0) {
            pnl_mat_get_row(currencyVolLine, parser->choleskyMatrix, parser->assetsSize+i-1);
            pnl_vect_mult_scalar(currencyVolLine, GET(parser->volatilities, parser->assetsSize+i-1));
            pnl_vect_plus_vect(assetVolLine, currencyVolLine);
        }
        RiskyAsset riskyAsset = RiskyAsset(assetVolLine, *interestRateModel);
        assets.push_back(riskyAsset);
    }

    // Update Domestic Interest Rate
    double domesticRate = GET(parser->interestRates, 0);
    domesticInterestRate = *new InterestRateModel(domesticRate);

    // Update Vector of Currencies
    for (int i = parser->assetsSize; i < parser->assetsSize+parser->currenciesSize; i++) {
        double foreignRate = GET(parser->interestRates, i-parser->assetsSize+1);
        InterestRateModel foreignInterestRateModel(foreignRate);
        pnl_mat_get_row(currencyVolLine, parser->choleskyMatrix, i);
        pnl_vect_mult_scalar(currencyVolLine, GET(parser->volatilities, i));
        Currency currency(currencyVolLine, domesticInterestRate, foreignInterestRateModel);
        currencies.push_back(currency);
    }
    // Update Cobstataion Dates
    monitoringTimeGrid = parser->datesManager;
    pnl_vect_free(&assetVolLine);
    pnl_vect_free(&currencyVolLine);
}

void GlobalModel::simulate_paths(PnlMat* past, PnlMat* path, int t, PnlRng* rng, bool isMonitoringDate) {
    pnl_mat_set_subblock(path, past, 0, 0);
    int timestep = 0;
    int assetsSize = assets.size();
    int currenciesSize = currencies.size();
    int index = monitoringTimeGrid->getNextFirstIndex(t);
    if (!isMonitoringDate) {
        PnlVect* gaussianVector = pnl_vect_create(path->n);
        pnl_vect_rng_normal(gaussianVector, path->n, rng);
        PnlVect* St = pnl_vect_create(path->n);
        pnl_mat_get_row(St, past, past->m-1);
        timestep = monitoringTimeGrid->at(index) - t;
        for (int j = 0; j < assetsSize; j++) {
          assets[j].sampleNextDate(GET(St, j) ,path, past->m-1, j, timestep, gaussianVector);
        }
        for (int j = 0; j < currenciesSize; j++) {
            currencies[j].sampleNextDate(GET(St, assetsSize+j), path, past->m-1, assetsSize+j, timestep, gaussianVector);
        }
    }

    for (int i = past->m; i < path->m; i++) {
        PnlVect* gaussianVector = pnl_vect_create(path->n);
        pnl_vect_rng_normal(gaussianVector, path->n, rng);
        // On respecte l'ordre des actifs comme dans le fichier .csv
        PnlVect* spots = pnl_vect_create(path->n);
        pnl_mat_get_row(spots, path, i-1);
        timestep = monitoringTimeGrid->at(index + 1) - monitoringTimeGrid->at(index);
        index++;
        for (int j = 0; j < assetsSize; j++) {
            assets[j].sampleNextDate(GET(spots, j), path, i, j, timestep, gaussianVector);
        }

        for (int j = 0; j < currenciesSize; j++) {
            currencies[j].sampleNextDate(GET(spots, assetsSize+j), path, i, assetsSize+j, timestep, gaussianVector);
        }
    }
}

void GlobalModel::shiftPaths(PnlMat* shiftedPath, double fdStep, int row, int col) {
    PnlVect* shiftedCol = pnl_vect_new();
    pnl_mat_get_col(shiftedCol, shiftedPath, col);
    for (int i = row; i < shiftedPath->m; i++) {
        LET(shiftedCol, i) = GET(shiftedCol, i) * (1 + fdStep);
    }
    pnl_mat_set_col(shiftedPath, shiftedCol, col);

}