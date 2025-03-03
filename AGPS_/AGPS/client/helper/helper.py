import pandas as pd


def assure_date_is_of_type_datetime(df):
    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"])
    
    return df