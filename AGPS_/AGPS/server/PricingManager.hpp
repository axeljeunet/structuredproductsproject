#pragma once

#include <iostream>
#include <nlohmann/json.hpp>
#include "pnl/pnl_vector.h"
#include "pnl/pnl_matrix.h"
#include "Parser.hpp"
#include "GlobalModel.hpp"
#include "MonteCarlo.hpp"

class PricingManager {
public:
    Parser* parser;
    GlobalModel* globalModel;
    MonteCarlo* monteCarlo;
    Option* option;

     PricingManager();
    ~PricingManager();
    void priceAndDeltas(PnlMat *past, double currentDate, bool isMonitoringDate, double &price, double &priceStdDev, PnlVect* &deltas, PnlVect* &deltasStdDev);
    void print();
    void updateData(Parser* theParser);
};
