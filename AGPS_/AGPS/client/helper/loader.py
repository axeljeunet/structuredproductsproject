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
        all_prices.fillna(method="ffill")
        all_returns.fillna(method="ffill")
        interest_rates.fillna(method="ffill")
        return MarketData(prices=all_prices, returns=all_returns, interest_rates=interest_rates)

    def get_volatility(start_date, end_date, market_data):
        data = market_data.returns[start_date:end_date]
        vols = data.std() * np.sqrt(252)
        corr = data.corr()
        return list(vols), corr.values.tolist()
    

    def get_adjusted_prices(t, is_monitoring_date, market_data, start_date, constatation_dates, constataion_int_dates, past=None):
        r_usd = market_data.interest_rates.loc[t, "RUSD"]
        r_hkd = market_data.interest_rates.loc[t, "RHKD"]
        prices = market_data.prices.loc[t]

        # Initialize past with the first row of prices at start_date
        past = [list(market_data.prices.loc[start_date])]
        
        if t == start_date:
            # Convert prices from USD/HKD to EUR where necessary
            for asset, curr in ASSET_CURRENCY_MAPPING.items():
                if curr != "EUR":
                    past[0][market_data.prices.columns.get_loc(asset)] *= prices.loc[curr]
            return past

        # Initialize past_df with start_date prices
        past_df = market_data.prices.loc[[start_date]]

        ind_const = 0
        int_dates_int_past = [0]

        # Ensure ind_const does not go out of bounds
        while ind_const < len(constatation_dates) and constatation_dates[ind_const] < t:
            int_dates_int_past.append(constataion_int_dates[ind_const])

            # Append the price row for constatation_dates[ind_const] properly
            past_df = pd.concat([past_df, market_data.prices.loc[[constatation_dates[ind_const]]]])

            ind_const += 1

        # Append the price row for the current time t
        past_df = pd.concat([past_df, market_data.prices.loc[[t]]])
        int_dates_int_past.append(len(pd.bdate_range(start=start_date, end=t)) - 1)

        # Convert non-EUR assets into EUR equivalents
        for asset, curr in ASSET_CURRENCY_MAPPING.items():
            if curr != "EUR":
                past_df[asset] = past_df[asset] * past_df[curr]

        # Apply exponential growth for RUSD and RHKD
        exp_factors = np.exp(np.array(int_dates_int_past)/252)
        past_df["XUSD"] = past_df["XUSD"] * exp_factors ** r_usd
        past_df["XHKD"] = past_df["XHKD"] * exp_factors ** r_hkd

        print(past_df)  # Debug print

        past = past_df.values.tolist()
        print(past)  # Debug print

        return past
