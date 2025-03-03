from dataclasses import dataclass
import pandas as pd


@dataclass
class MarketData:
    prices: pd.DataFrame
    returns: pd.DataFrame
    interest_rates: pd.DataFrame

    def summary(self):
        """Retourne un résumé des tableaux."""
        return {
            "prices": {
                "rows": len(self.prices),
                "columns": list(self.prices.columns),
            },
            "returns": {
                "rows": len(self.returns),
                "columns": list(self.returns.columns),
            },
            "interest_rates": {
                "rows": len(self.interest_rates),
                "columns": list(self.interest_rates.columns)
            }
        }