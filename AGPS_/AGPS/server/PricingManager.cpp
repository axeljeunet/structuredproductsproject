#include <iostream>
#include "json_reader.hpp"
#include "PricingManager.hpp"

PricingManager::PricingManager(): parser(new Parser()) {
    globalModel = new GlobalModel();
    option = new Option();
    monteCarlo = new MonteCarlo(option, globalModel);
}

PricingManager::~PricingManager() {}

void PricingManager::print() {
    /**std::cout << "nAssets: " << nAssets << std::endl;
    std::cout << "fdStep: " << fdStep << std::endl;
    std::cout << "nSamples: " << nSamples << std::endl;
    std::cout << "strikes: ";
    pnl_vect_print_asrow(strikes);
    std::cout << "paymentDates: ";
    pnl_vect_print_asrow(paymentDates);
    std::cout << "volatility: ";
    pnl_mat_print(volatility);**/
}

void PricingManager::updateData(Parser *theParser) {
    parser = theParser;
    globalModel->updateGlobalModel(theParser);
    option->updateOption(theParser);
    monteCarlo->updateMonteCarlo(*option, *globalModel, *theParser);
}

void PricingManager::priceAndDeltas(PnlMat *past, double currentDate, bool isMonitoringDate,
    double &price, double &priceStdDev, PnlVect* &deltas, PnlVect* &deltasStdDev) {
    monteCarlo->priceAndDelta(past, (int) currentDate, isMonitoringDate, price, priceStdDev, deltas, deltasStdDev);
}