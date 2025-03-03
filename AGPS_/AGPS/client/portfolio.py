from typing import List
import numpy as np

class Portfolio:

    def __init__(self):
        self.composition: List = []
        self.value = 0
        self.cash = 0

    def get_composition(self):
        """Retourne la liste des positions du portefeuille."""
        return self.composition

    def compute_portoflio_value(self, spots):
        self.value = self.cash + self.get_assets_value(spots)

    def get_assets_value(self, spots):
        return np.dot(np.array(spots), np.array(self.composition))

    def discount(self, interest_rate, delta_t):
        return np.exp(interest_rate * delta_t / 252)

    def update_portfolio(self, new_spots, new_deltas, delta_t, interest_rate):
        self.cash = self.cash * self.discount(interest_rate, delta_t)
        self.cash += np.dot(np.array(self.composition) - np.array(new_deltas), new_spots)
        self.composition = new_deltas
        self.value = self.compute_portoflio_value(new_spots)
    
    def __repr__(self):
        return f"Portfolio(positions={self.composition})"
