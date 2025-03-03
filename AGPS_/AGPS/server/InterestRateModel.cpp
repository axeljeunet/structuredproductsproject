#include "InterestRateModel.hpp"
#include <cmath>
#include <iostream>


// Constructeur
InterestRateModel::InterestRateModel() {}

InterestRateModel::InterestRateModel(double rate)
    : interestRate(rate) {}

// Méthode pour obtenir le taux de discount entre deux dates
double InterestRateModel::discount(double t1, double t2) const {
    return exp(-interestRate * (t2 - t1)/252);
}

// Méthode pour obtenir la valeur d'un compte entre deux dates
double InterestRateModel::account(double t1, double t2) const {
    return exp(interestRate * (t2 - t1)/252);
}
