#include "Parser.hpp"
#include <fstream>
#include <iostream>


Parser::Parser() {}
Parser::Parser(const char* jsonFile) {
    std::ifstream ifs(jsonFile);
    nlohmann::json jsonParams = nlohmann::json::parse(ifs);
    currenciesSize = 2;
    assetsSize = 3;

    // Volatilities
    std::vector<double> volatilitiesVector = jsonParams.at("Volatilities").get<std::vector<double>>();
    volatilities = pnl_vect_create_from_ptr(volatilitiesVector.size(), volatilitiesVector.data());

    // Interest Rates
    std::vector<double> ratesVector = jsonParams.at("Interest Rates").get<std::vector<double>>();
    interestRates = pnl_vect_create_from_ptr(ratesVector.size(), ratesVector.data());

    // Maturity
    maturityInDays = jsonParams.at("Maturity").get<int>();

    // Constatation Dates
    std::vector<double> fixingDatesStdVector = jsonParams.at("Constatation Dates").get<std::vector<double>>();
    PnlVect* fixingDatesVector = pnl_vect_create_from_ptr(fixingDatesStdVector.size(), fixingDatesStdVector.data());
    datesManager = new TimeGrid(fixingDatesVector);

    // Correlation Matrix + Cholesky Matrix
    auto correlations = jsonParams.at("Correlations");
    size_t rows = correlations.size();
    size_t cols = rows > 0 ? correlations[0].size() : 0;
    correlationMatrix = pnl_mat_create(rows, cols);
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            MLET(correlationMatrix, i, j) = correlations[i][j].get<double>();
        }
    }
    choleskyMatrix = pnl_mat_copy(correlationMatrix);
    pnl_mat_chol(choleskyMatrix);

}

Parser::~Parser() {
    // Libération des ressources allouées dynamiquement
}
