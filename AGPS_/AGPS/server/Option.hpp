#ifndef OPTION_HPP
#define OPTION_HPP

#include "TimeGrid.hpp"
#include "InterestRateModel.hpp"
#include <vector>
#include <string>
#include "pnl/pnl_vector.h"
#include "Parser.hpp"

class Option {
public:
    // Attributs
    std::vector<int> assetCurrencyMapping;
    std::vector<InterestRateModel> foreignInterestRates;
    InterestRateModel domesticInterestRate;
    TimeGrid* monitoringTimeGrid;
    double valeurLiquidativeInitiale= 1000;

    // Constructeur
    Option(const std::vector<int>& assetCurrencyMapping,
           const std::vector<InterestRateModel>& foreignInterestRates,
           const InterestRateModel& domesticInterestRate,
           TimeGrid* monitoringTimeGrid);

    Option();
    // Méthode virtuelle pure pour calculer le payoff
    PnlVect* payoff(PnlMat *path, double time) const;
    void updateOption(Parser* parser);
    void createPathsInLocalCurrency(PnlMat *path, PnlMat* newPath) const;
    ~Option() {}
};

#endif //OPTION_HPP