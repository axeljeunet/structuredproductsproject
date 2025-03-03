#ifndef PARSER_HPP
#define PARSER_HPP
#include <string>
#include <vector>
#include <nlohmann/json.hpp>
#include "pnl/pnl_vector.h"
#include "pnl/pnl_matrix.h"
#include "TimeGrid.hpp"

class Parser {

public:
    PnlVect* interestRates;
    PnlVect* volatilities;
    int maturityInDays;
    PnlMat* correlationMatrix;
    PnlMat* choleskyMatrix;
    int assetsSize;
    double fdStep = 0.1;
    int sampleNb = 10000;
    int currenciesSize;
    TimeGrid* datesManager;

    explicit Parser(const char* jsonFile);
    Parser();


    ~Parser();
};



#endif //PARSER_HPP
