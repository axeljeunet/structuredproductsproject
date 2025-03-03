from AGPS_.AGPS.client.models.portfolio import Portfolio

class Hedger:
    def __init__(self, cash=0.0):
        """
        Initialise le Hedger avec un portefeuille et un montant de cash initial.
        :param portfolio: Instance de la classe Portfolio
        :param cash: Montant de cash disponible pour le hedging
        """
        self.portfolio = Portfolio()
        self.cash = cash

    def hedge(self, market_data):
        """
        Effectue le hedging en ajustant les positions du portefeuille.
        :param market_data: Données de marché contenant les prix actuels des actifs
        """
        if not self.portfolio.positions:
            print("⚠️ Aucune position dans le portefeuille, rien à hedger.")
            return

        print("📊 Début du hedging...")
        for position in self.portfolio.positions:
            # Exemple : Ajuster les deltas en fonction du marché
            new_deltas = self.calculate_new_deltas(position, market_data)
            
            # Mise à jour des positions dans le portefeuille
            position.deltas = new_deltas

            # Mise à jour du cash en fonction des ajustements
            self.update_cash(new_deltas)

        print(f"✅ Hedging terminé. Nouveau cash disponible: {self.cash:.2f}")

    def calculate_new_deltas(self, position, market_data):
        """
        Calcule les nouveaux deltas en fonction du marché.
        :param position: Instance de la classe Position
        :param market_data: Données de marché
        :return: Nouvelle liste de deltas ajustés
        """
        # Simulation : On ajuste légèrement les deltas en fonction du marché
        new_deltas = [delta * 1.05 for delta in position.deltas]  # Exemple : Augmentation de 5%
        return new_deltas

    def update_cash(self, new_deltas):
        """
        Met à jour le cash en fonction des ajustements de hedging.
        :param new_deltas: Liste des nouveaux deltas après hedging
        """
        # Simulation : Supposons que chaque delta ajusté coûte un montant proportionnel
        self.cash -= sum(new_deltas) * 10  # Exemple : coût fictif de 10 unités par delta ajusté

    def __repr__(self):
        return f"Hedger(portfolio={self.portfolio}, cash={self.cash:.2f})"
