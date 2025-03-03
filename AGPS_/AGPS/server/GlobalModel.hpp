#ifndef GLOBALMODEL_HPP
#define GLOBALMODEL_HPP

#include <vector>
#include "RiskyAsset.hpp"  // Inclure pour RiskyAssets
#include "Currency.hpp"    // Inclure pour Currency
#include "TimeGrid.hpp"   // Inclure pour ITimeGrid
#include "InterestRateModel.hpp"  // Inclure pour InterestRateModel
#include "Parser.hpp"

class GlobalModel {
public:
    // Vecteur d'actifs risqués
    std::vector<RiskyAsset> assets;

    // Vecteur de devises
    std::vector<Currency> currencies;

    // Grille de temps pour la surveillance
    TimeGrid* monitoringTimeGrid;

    // Modèle de taux d'intérêt domestique
    InterestRateModel domesticInterestRate;

    // Constructeur
    GlobalModel(
        const std::vector<RiskyAsset>& assets,
        const std::vector<Currency>& currencies,
        TimeGrid* monitoringTimeGrid,
        const InterestRateModel& domesticInterestRate
    );

    GlobalModel();

    // Destructeur
    ~GlobalModel();

    void simulate_paths(PnlMat* past, PnlMat* path, int t, PnlRng* rng, bool isMonitoringDate);
    void shiftPaths(PnlMat* shiftedPath, double fdStep, int row, int col);
    void updateGlobalModel(Parser* parser);
};

#endif
