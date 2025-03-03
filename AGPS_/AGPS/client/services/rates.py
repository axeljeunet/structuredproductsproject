import pandas as pd
from warehouse.market_data import MarketData

def get_all_rates_by_dates(market_data: MarketData, list_dates: pd.Series) -> pd.DataFrame:
    list_dates = pd.to_datetime(list_dates)
    rates_data = market_data.rates
    rates = rates_data.loc[rates_data["Date"].isin(list_dates)]
    return rates

def get_prices_by_indexes_and_dates(market_data: MarketData, list_dates: pd.Series,
                                     list_rates: pd.Series) ->pd.DataFrame:
    list_dates = pd.to_datetime(list_dates)
    rates_data = market_data.rates
    rates = rates_data.loc[rates_data["Date"].isin(list_dates) 
                            & rates_data["RateName"].isin(list_rates)]
    return rates

