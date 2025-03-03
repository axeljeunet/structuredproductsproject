import pickle
from warehouse.market_data import MarketData
import os

class DataStorage:
    @staticmethod
    def save_to_file(market_data: MarketData, file_path: str):
        """
        Sauvegarde les tableaux dans un fichier binaire.
        """
        resolved_path = os.path.expanduser(file_path)
        
        with open(resolved_path, "wb") as f:
            pickle.dump(market_data, f)
        print(f"Données sauvegardées dans {resolved_path}")

    @staticmethod
    def load_from_file(file_path: str) -> MarketData:
        """
        Charge les tableaux depuis un fichier binaire.
        """
        with open(file_path, "rb") as f:
            market_data = pickle.load(f)
        print(f"Données chargées depuis {file_path}")
        return market_data
