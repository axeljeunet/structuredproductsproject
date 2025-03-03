import pandas as pd
from models.market_data import MarketData


def assure_date_is_of_type_datetime(df):
    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"])
    
    return df


def get_all_prices_by_dates(market_data: MarketData, list_dates: pd.Series) -> pd.DataFrame:
    list_dates = pd.to_datetime(list_dates)
    index_data = market_data.index
    prices = index_data.loc[index_data["Date"].isin(list_dates)]
    return prices

def get_prices_by_indexes_and_dates(market_data: MarketData, list_dates: pd.Series,
                                     list_indexes: pd.Series) ->pd.DataFrame:
    list_dates = pd.to_datetime(list_dates)
    index_data = market_data.index
    prices = index_data.loc[index_data["Date"].isin(list_dates) 
                            & index_data["Instrument"].isin(list_indexes)]
    return prices

