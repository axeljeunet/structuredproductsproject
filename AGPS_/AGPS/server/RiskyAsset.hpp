#ifndef RISKY_ASSET_HPP
#define RISKY_ASSET_HPP

#include "RiskyDynamics.hpp"
#include "InterestRateModel.hpp"
#include <pnl/pnl_vector.h>
#include <pnl/pnl_matrix.h>

class RiskyAsset : public RiskyDynamics {
public:
    InterestRateModel domesticInterestRate;  // Attribut pour le taux d'intérêt domestique

    // Constructeur
    RiskyAsset();
    RiskyAsset(PnlVect* volatility, InterestRateModel domesticRate);

    // Destructeur
    ~RiskyAsset() override;
};

#endif