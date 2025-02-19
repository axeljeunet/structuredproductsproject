from models.AbstractModel import AbstractModel
import numpy as np
import pandas as pd
from scipy.optimize import minimize
import matplotlib.pyplot as plt
from scipy.stats import norm
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import statsmodels.api as sm

class RateModel(AbstractModel):

    def __init__(self, rates, window_size=252):
        self.window_size = window_size
        self.parameters_history = None
        self.rates = rates


    def estimate_paramters(self):

        # Transformation des données
        rates = self.rates[(self.rates["Date"].dt.year >= 2000)
                              & (self.rates["Date"].dt.year <= 2016)]
        rates = rates[["Date", "REUR"]].reset_index(drop=True)
        rates = rates.sort_values("Date")  # Trier par date au cas où
        rates["dt"] = (rates["Date"].diff().dt.days).fillna(1) / 252  # En années
        rates["dr"] = rates["REUR"].diff()  # Calcul des variations de taux

        # Supprimer la première ligne (NaN après diff)
        rates = rates.dropna().reset_index(drop=True)

        # Variables pour la régression
        X = rates["REUR"]  # rt (taux d'intérêt actuel)
        y = rates["dr"] / rates["dt"]  # dr/dt (taux de variation)

        # Ajouter une constante pour estimer 'a'
        X = sm.add_constant(X)  # Ajoute une colonne de 1 pour estimer a

        # Régression OLS
        model = sm.OLS(y, X).fit()
        a_est = model.params["const"]  # a estimé
        b_est = -model.params["REUR"]  # b estimé (avec le bon signe)

        # Calcul de sigma à partir des résidus de la régression
        residuals = model.resid
        sigma_est = np.std(residuals * np.sqrt(rates["dt"]))

        # Affichage des résultats
        print(f"Paramètres estimés : a = {a_est:.6f}, b = {b_est:.6f}, sigma = {sigma_est:.6f}")
        print(model.summary())  # Affiche le résumé complet de la régression
        return a_est, b_est, sigma_est
    
    def simulate_paths(self, a_est, b_est, sigma_est):
        # Paramètres estimés (issus de la calibration)
        a = a_est
        b = b_est
        sigma = sigma_est

        # Paramètres de simulation
        start_date = "2017-01-01"
        end_date = "2020-12-31"
        dt = 1 / 252  # Pas de temps journalier en années
        n_steps = (pd.to_datetime(end_date) - pd.to_datetime(start_date)).days
        n_steps = int(n_steps * (252 / 365))  # Conversion en jours de marché

        # Initialisation
        r0 = self.rates["REUR"].loc[self.rates["Date"]==pd.to_datetime("2016-12-30")]  # Dernière valeur observée de 2016
        simulated_rates = [r0]
        dates = pd.date_range(start=start_date, periods=n_steps, freq="B")  # Jours ouvrés

        # Simulation de Vasicek
        for _ in range(1, n_steps):
            epsilon = np.random.normal(0, 1)  # Tirage gaussien
            dr = (a - b * simulated_rates[-1]) * dt + sigma * np.sqrt(dt) * epsilon
            simulated_rates.append(simulated_rates[-1] + dr)

        # Stocker les résultats dans un DataFrame
        simulated_df = pd.DataFrame({"Date": dates, "Simulated Rates": simulated_rates})
    
        # Extraire les taux réels entre 2017 et 2020
        real_rates = self.rates[(self.rates["Date"].dt.year >= 2017) &
                                (self.rates["Date"].dt.year <= 2020)]
        real_rates = real_rates[["Date", "REUR"]].reset_index(drop=True)
        real_rates.to_csv("~/3aif/AGPS/real_rates.csv")
        # Tracer les taux simulés
        plt.figure(figsize=(12, 6))
        plt.plot(list(simulated_df["Date"]), list(simulated_df["Simulated Rates"]), label="Taux simulés (Vasicek)", color="blue")

        # Tracer les taux réels
        plt.plot(list(real_rates["Date"]), list(real_rates["REUR"]), label="Taux réels", color="red", linestyle="dashed")

        # Mise en forme
        plt.xlabel("Date")
        plt.ylabel("Taux d'intérêt")
        plt.title("Comparaison des taux simulés et réels (2017-2020)")
        plt.legend()
        plt.grid()
        plt.show()

        return simulated_df