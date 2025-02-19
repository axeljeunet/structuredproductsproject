import pandas as pd
from warehouse.market_data import MarketData
from helper.helper import assure_date_is_of_type_datetime
import numpy as np
import math as m


ASSET_CURRENCY_MAPPING = {"EUROSTOXX50": "EUR", "SP500": "XUSD", "HANGSENG": "XHKD"}

class DataLoader:
    @staticmethod
    def load_from_file(filename: str) -> MarketData:
        """
        Charge les données depuis un fichier Excel et retourne un objet MarketData.
        """
        data = pd.ExcelFile(filename)
        index_price = data.parse("ClosePrice")
        index_price = index_price[["Date", "EUROSTOXX50", "SP500", "HANGSENG"]]
        # index_melted = pd.melt(index_data, id_vars = ["Date"], var_name="Instrument",
        #                         value_name="Price")
        index_price = assure_date_is_of_type_datetime(index_price)

        index_returns = data.parse("CloseRet")
        index_returns = index_returns[["Date", "EUROSTOXX50", "SP500", "HANGSENG"]]
        # index_returns_melted = pd.melt(index_returns, id_vars = ["Date"], var_name="Instrument",
        #                         value_name="Return")
        index_returns = assure_date_is_of_type_datetime(index_returns)
        #index_melted = pd.merge(index_melted, index_returns_melted, how="left", on=["Date", "Instrument"])

        interest_rates = data.parse("TauxInteret")
        interest_rates = interest_rates[["Date", "REUR", "RUSD", "RHKD"]]
        interest_rates = assure_date_is_of_type_datetime(interest_rates)

        xfor_price = data.parse("XFORPrice")
        xfor_price = xfor_price[["Date", "XUSD", "XHKD"]]
        xfor_price = assure_date_is_of_type_datetime(xfor_price)
        
        xfor_returns = data.parse("XFORRet")
        xfor_returns = xfor_returns[["Date", "XUSD", "XHKD"]]
        xfor_returns = assure_date_is_of_type_datetime(xfor_returns)
        # xfor_returns_melted = pd.melt(xfor_returns, id_vars = ["Date"], var_name="RateName",
        #                         value_name="RateReturn")

        #rates_data = pd.merge(rates_data, xfor_data, how="left", on="Date")

        # Process rates data
        # rates_melted = pd.melt(rates_data, id_vars=["Date"], var_name="RateName",
        #                         value_name="RateValue")
        # rates_melted = assure_date_is_of_type_datetime(rates_melted)

        # rates_melted = pd.merge(rates_melted, xfor_returns_melted, how="left", on=["Date", "RateName"])        
        all_prices = pd.merge(index_price, xfor_price, how="inner")
        all_returns = pd.merge(index_returns, xfor_returns, how="inner")
        all_prices = all_prices.set_index("Date", drop=True)
        all_returns = all_returns.set_index("Date", drop=True)
        interest_rates = interest_rates.set_index("Date", drop=True)
        return MarketData(prices=all_prices, returns=all_returns, interest_rates=interest_rates)

    def get_volatility(start_date, end_date, market_data):
        data = market_data.returns[start_date:end_date]
        vols = data.std() * np.sqrt(252)
        corr = data.corr()
        return vols, corr
    
    def get_adjusted_prices(t, is_monitoring_date, market_data, start_date, past = None):
        
        r_usd = market_data.interest_rates.loc[t, "RUSD"]
        r_hkd = market_data.interest_rates.loc[t, "RHKD"]
        prices = market_data.prices.loc[t]
        if t == start_date:
            past = [list(market_data.prices.loc[start_date])]
            counter = 0
            for asset, curr in ASSET_CURRENCY_MAPPING.items():
                if curr != "EUR":
                    past[0][counter] = prices.loc[asset] * prices.loc[curr]
                counter += 1
            return past
        


