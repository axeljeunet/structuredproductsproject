import pandas as pd
from warehouse.market_data import MarketData
from services.index import get_all_prices_by_dates, get_prices_by_indexes_and_dates

def test_get_all_prices_by_dates():
    data = {
        "Date": ["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-01", "2023-01-02", "2023-01-03"],
        "Instrument": ["EUROSTOXX50", "EUROSTOXX50", "EUROSTOXX50", "SP500", "SP500", "SP500"],
        "Price": [100, 101, 102, 200, 201, 202]
    }
    index_data = pd.DataFrame(data)
    index_data["Date"] = pd.to_datetime(index_data["Date"])
    market_data = MarketData(index=index_data, rates=None, bonds=None)

    list_dates = pd.Series(["2023-01-01", "2023-01-03"])
    result = get_all_prices_by_dates(market_data, list_dates)
    print(result)


def test_get_prices_by_indexes_and_dates():
        data = {
            "Date": ["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-01", "2023-01-02", "2023-01-03"],
            "Instrument": ["EUROSTOXX50", "EUROSTOXX50", "EUROSTOXX50", "SP500", "SP500", "SP500"],
            "Price": [100, 101, 102, 200, 201, 202]
        }
        index_data = pd.DataFrame(data)
        index_data["Date"] = pd.to_datetime(index_data["Date"])

        market_data = MarketData(index=index_data, rates=None, bonds=None)
        list_dates = pd.Series(["2023-01-01", "2023-01-03"])
        list_indexes = pd.Series(["EUROSTOXX50"])

        result = get_prices_by_indexes_and_dates(market_data, list_dates, list_indexes)
        print(result)
