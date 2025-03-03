#ifndef TIMEGRID_HPP
#define TIMEGRID_HPP

#include "pnl/pnl_vector.h"
#include <vector>
#include <string>
#include <stdexcept>

// Classe de base virtuelle pour gérer une grille de temps
class TimeGrid {
public:

    // Vecteur qui contient les dates
    PnlVect* dates;

    TimeGrid();
    TimeGrid(PnlVect* dates);
    ~TimeGrid();

    // Retourne la date à un index donné
    int at(int index) const;

    // Retourne le nombre d'éléments dans la grille
    int len() const;

    // Vérifie si une date existe à l'indice donné
    bool has(int nDays) const;

    int getNextFirstIndex(int t);
};

#endif