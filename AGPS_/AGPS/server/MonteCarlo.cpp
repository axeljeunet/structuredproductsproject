#include "MonteCarlo.hpp"
#include <iostream>

// Constructeur
MonteCarlo::MonteCarlo(Option* option, GlobalModel model, Parser* parser)
    : option(option), model(model), parser(parser) {
          rng = pnl_rng_create(PNL_RNG_MERSENNE);
          pnl_rng_sseed(rng, 0);
    }

MonteCarlo::MonteCarlo(Option* option, GlobalModel* model)
    : model(*model), option(option) {
    rng = pnl_rng_create(PNL_RNG_MERSENNE);
    pnl_rng_sseed(rng, 0);
}

void MonteCarlo::updateMonteCarlo(Option& product, GlobalModel& globalModel, Parser& myParser) {
    option = &product;
    model = globalModel;
    parser = &myParser;
}

// Méthode pour calculer le prix et les deltas
void MonteCarlo::priceAndDelta(PnlMat* past, int t, bool isMonitoringDate, double& price, double& priceStdDev, PnlVect* deltas, PnlVect* deltasStdDev) {
    // Implémenter la logique pour la simulation Monte Carlo
    std::cout << "Simulation en cours..." << std::endl;
    // Code de simulation
    double fdStep = parser->fdStep;
    int index = model.monitoringTimeGrid->getNextFirstIndex(t);
    PnlVect* assetsAtTimet = pnl_vect_new();
    pnl_mat_get_row(assetsAtTimet, past, past->m-1);
    PnlMat* path = pnl_mat_create(option->monitoringTimeGrid->dates->size, past->n);
    PnlMat* shiftedPathPlus = pnl_mat_create(option->monitoringTimeGrid->dates->size, past->n);
    PnlMat* shiftedPathMinus = pnl_mat_create(option->monitoringTimeGrid->dates->size, past->n);
    PnlVect* flux = pnl_vect_create_from_zero(5);
    for (int i = 0; i < parser->sampleNb; i++) {
        model.simulate_paths(past, path, t, rng, isMonitoringDate);
        pnl_vect_plus_vect(flux, option->payoff(path, t));
        //double payoffValue = option->payoff(path, t);
        double payoffValue = GET(flux, 4);
        price += payoffValue;
		priceStdDev += payoffValue * payoffValue;
        /**for (int asset = 0; asset < past->n; asset++) {
            pnl_mat_clone(shiftedPathPlus, path);
            pnl_mat_clone(shiftedPathMinus, path);
            model.shiftPaths(shiftedPathPlus, fdStep, index, asset);
            model.shiftPaths(shiftedPathMinus, -fdStep, index, asset);
            double diffPayoff = option->payoff(shiftedPathPlus, t) - option->payoff(shiftedPathMinus, t);
            LET(deltas, asset) = GET(deltas, asset) + diffPayoff;
            LET(deltasStdDev, asset) = GET(deltasStdDev, asset) + diffPayoff * diffPayoff;
        }**/
    }
    pnl_vect_div_scalar(flux, parser->sampleNb);
    price = GET(flux, 4);
    //price = price / parser->sampleNb;
    pnl_vect_print(flux);
    std::cout << "interest rate " << model.domesticInterestRate.interestRate << std::endl;
    std::cout << "maturity " << parser->maturityInDays << std::endl;
	priceStdDev = abs(priceStdDev/parser->sampleNb - price * price);
    priceStdDev = std::sqrt(priceStdDev / parser->sampleNb);
    /**for (int asset = 0; asset < past->n; asset++) {
        double Std = GET(assetsAtTimet, asset);
        LET(deltas, asset) = GET(deltas, asset) / (2*Std*parser->sampleNb*fdStep);
        LET(deltasStdDev, asset) = abs(GET(deltasStdDev, asset)/(4*Std*Std*parser->sampleNb*fdStep*fdStep)
                    - GET(deltas, asset) * GET(deltas, asset));
        LET(deltasStdDev, asset) = std::sqrt(GET(deltasStdDev, asset) / parser->sampleNb);

    }**/

}
