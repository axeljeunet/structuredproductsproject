from population.loader import DataLoader
from population.storage import DataStorage
from tests.test_services import test_get_all_prices_by_dates, test_get_prices_by_indexes_and_dates
from models.RateModel import RateModel
import pandas as pd
import datetime
import numpy as np

def main():
    # Charger les données depuis Excel
    file_path = "~/3aif/AGPS/DonneesGPS2025.xlsx"
    market_data = DataLoader.load_from_file(file_path)
    # print("Résumé des données chargées :", market_data.summary())
    # print(market_data.prices.head())
    # print(market_data.returns.head())
    # print(market_data.interest_rates.head())

    constatation_dates = [datetime.datetime(year=2006, month=1, day=4),
                datetime.datetime(year=2007, month=1, day=4),
                datetime.datetime(year=2008, month=1, day=4),
                datetime.datetime(year=2009, month=1, day=5),
                datetime.datetime(year=2010, month=1, day=4)
                ]
    # print(datetime.datetime(year=2006, month=1, day=4) in constatation_dates)
    start_date = datetime.datetime(year=2005, month=1, day=4)
    end_date = datetime.datetime(year=2010, month=1, day=4)
    vols, corr = DataLoader.get_volatility(start_date, end_date, market_data)
    past = DataLoader.get_adjusted_prices(start_date, True, market_data, start_date)
    interest_rates = list(market_data.interest_rates.loc[start_date])
    maturity_in_days = pd.bdate_range(start=start_date, end=end_date)
    const_int_dates = [0]
    for i in range(len(constatation_dates)):
        const_int_dates.append(pd.bdate_range(start=start_date, end=constatation_dates[i]))

    json_data = {
        "InterestRates": interest_rates,
        "Volatilities": vols,
        "Correlations": corr,
        "constatationDates": const_int_dates,
        "maturity": maturity_in_days
    }

if __name__ == "__main__":
    
    main()
