#include "TimeGrid.hpp"

TimeGrid::TimeGrid() {
  dates = nullptr;
}
TimeGrid::TimeGrid(PnlVect* datesVect) {
    if (datesVect != NULL) {
        dates = pnl_vect_copy(datesVect);
    }
}

int TimeGrid::at(int index) const{
    if (index < 0 || index >= dates->size) {
        throw std::invalid_argument("index out of range");
    }
    return (int) GET(dates, index);
}

int TimeGrid::len() const {
    return dates->size;
}

// Vérifier si une date existe à l'indice donné
bool TimeGrid::has(int nDays) const {
    for (int i = 0; i < dates->size; i++) {
        int day = GET(dates, i);
        if (day == nDays) {
            return true;
        }
    }
    return false;
}

int TimeGrid::getNextFirstIndex(int t) {
    int index = 0;
    while (index < len() and GET(dates, index) < t) {
        index++;
    }
    return index;
}

TimeGrid::~TimeGrid() {
    //pnl_vect_free(&dates);
}