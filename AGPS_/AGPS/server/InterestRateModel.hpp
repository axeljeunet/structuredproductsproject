#ifndef INTEREST_RATE_MODEL_HPP
#define INTEREST_RATE_MODEL_HPP

#include <cmath>
#include <iostream>

class InterestRateModel {
public:

    double interestRate;

    // Constructeur
    InterestRateModel(double rate);
    InterestRateModel();

    // Méthode pour obtenir le taux de discount entre deux dates
    double discount(double t1, double t2) const;

    // Méthode pour obtenir la valeur d'un compte entre deux dates
    double account(double t1, double t2) const;

};

#endif
