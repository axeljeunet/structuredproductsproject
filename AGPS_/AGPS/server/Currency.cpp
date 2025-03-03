#include "Currency.hpp"
#include "InterestRateModel.hpp"

// Constructeur
Currency::Currency(PnlVect* volatility, InterestRateModel domesticRate, InterestRateModel foreignRate)
    : RiskyDynamics(domesticRate.interestRate, volatility),
      foreignInterestRate(foreignRate),
      domesticInterestRate(domesticRate) {}

Currency::Currency()
    : RiskyDynamics(),
      foreignInterestRate(InterestRateModel(0.0)),
      domesticInterestRate(InterestRateModel(0.0)) {}

InterestRateModel Currency::getDomesticInterestRate() const {
    return domesticInterestRate;
}

InterestRateModel Currency::getForeignInterestRate() const {
    return foreignInterestRate;
}

Currency::~Currency() {}