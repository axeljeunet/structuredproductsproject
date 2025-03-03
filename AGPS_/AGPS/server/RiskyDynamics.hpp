#ifndef RISKY_DYNAMICS_HPP
#define RISKY_DYNAMICS_HPP

#include <pnl/pnl_vector.h>
#include <pnl/pnl_matrix.h>
#include <pnl/pnl_random.h>

class RiskyDynamics {
public:
    double drift;                // Dérive des actifs risqués
    PnlVect* volatilityVector;    // Vecteur de volatilité des actifs risqués

    // Constructeur
    RiskyDynamics();
    RiskyDynamics(double drift, PnlVect* volatility);

    // Destructeur
    virtual ~RiskyDynamics();

    // Méthode pour échantillonner la prochaine date de l'actif risqué
    void sampleNextDate(double spot, PnlMat* path, int i, int j, int timestep, PnlVect* gaussianVector) const;
};

#endif