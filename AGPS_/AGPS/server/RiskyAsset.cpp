#include "RiskyAsset.hpp"
#include <cmath>
#include <iostream>

// Constructeur
RiskyAsset::RiskyAsset()
    : RiskyDynamics(), domesticInterestRate(InterestRateModel(0.0)) {}

RiskyAsset::RiskyAsset(PnlVect* volatility, InterestRateModel domesticRate)
    : RiskyDynamics(domesticRate.interestRate, volatility), domesticInterestRate(domesticRate) {}

// Destructeur
RiskyAsset::~RiskyAsset() {
    // Les objets de la classe parente RiskyDynamics sont automatiquement libérés
}