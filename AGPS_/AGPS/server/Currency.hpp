#ifndef CURRENCY_HPP
#define CURRENCY_HPP

#include "RiskyDynamics.hpp"
#include "InterestRateModel.hpp"

class Currency : public RiskyDynamics {
    public:
        InterestRateModel foreignInterestRate;
        InterestRateModel domesticInterestRate;

        // Constructeur
        Currency(PnlVect* volatility, InterestRateModel domesticRate, InterestRateModel foreignRate);
        Currency();
        // Destructeur
        ~Currency() override;

        // Méthode pour obtenir le taux de change
        InterestRateModel getDomesticInterestRate() const;
        InterestRateModel getForeignInterestRate() const;
};

#endif