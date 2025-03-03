#ifndef MONTE_CARLO_HPP
#define MONTE_CARLO_HPP

#include "Option.hpp"
#include "GlobalModel.hpp"
#include "Parser.hpp"

class MonteCarlo {
public:
    Option* option;
    GlobalModel model;
    Parser* parser;
    PnlRng* rng;

    // Constructeur
    MonteCarlo(Option* option, GlobalModel model, Parser* parser);
    MonteCarlo(Option* option, GlobalModel* model);

    // Méthode pour calculer le prix et les deltas
    void priceAndDelta(PnlMat* past, int t, bool isMonitoringDate, double& price, double& priceStdDev, PnlVect* deltas, PnlVect* deltasStdDev);
    void updateMonteCarlo(Option& product, GlobalModel& globalModel, Parser& myParser);
};

#endif

