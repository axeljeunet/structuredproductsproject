from helper.loader import DataLoader
from helper.storage import DataStorage
from tests.test_services import test_get_all_prices_by_dates, test_get_prices_by_indexes_and_dates
import pandas as pd
import datetime
import numpy as np
import pricing_pb2
import pricing_pb2_grpc
import json
import os
import grpc

# Charger les données depuis Excel
MARKET_DATA_PATH = "AGPS_/AGPS/DonneesGPS2025.xlsx"
MARKET_DATA = DataLoader.load_from_file(MARKET_DATA_PATH)

# Convertir ~ en chemin absolu
JSON_FILE_PATH = os.path.expanduser("AGPS_/AGPS/fichier_in.json")

END_DATE = datetime.datetime(year=2014, month=1, day=6)

CONSTATION_DATES = [
    datetime.datetime(year=2010, month=1, day=4),
    datetime.datetime(year=2011, month=1, day=4),
    datetime.datetime(year=2012, month=1, day=4),
    datetime.datetime(year=2013, month=1, day=4),
    datetime.datetime(year=2014, month=1, day=6)
]

SERVER_ADDRESS = "localhost:50051"
CHANNEL = grpc.insecure_channel(SERVER_ADDRESS)
STUB = pricing_pb2_grpc.GrpcPricerStub(CHANNEL)

def rebalancing_information(start_date):
    return

def information(start_date):
    return

def rebalance(start_date):
    return

def get_pricing_input(start_date):
    const_int_dates = [0]  # Début à 0 pour le premier point
    for date in CONSTATION_DATES:
        business_days_count = len(pd.bdate_range(start=start_date, end=date)) - 1  # -1 pour exclure start_date
        const_int_dates.append(business_days_count)

    # print(datetime.datetime(year=2006, month=1, day=4) in constatation_dates)
    vols, corr = DataLoader.get_volatility(datetime.datetime(year=2000, month=1, day=3), start_date, MARKET_DATA)
    print(vols)
    past = DataLoader.get_adjusted_prices(start_date, True, MARKET_DATA, start_date, CONSTATION_DATES, const_int_dates)
    interest_rates = list(MARKET_DATA.interest_rates.loc[start_date])
    print(interest_rates)

    maturity_in_days = len(pd.bdate_range(start=start_date, end=END_DATE)) - 1

    json_data = {
        "Interest Rates": interest_rates,
        "Volatilities": vols,
        "Correlations": corr,
        "Constatation Dates": const_int_dates,
        "Maturity": maturity_in_days
    }

    # Créer le fichier et écrire les données JSON
    with open(JSON_FILE_PATH, "w") as json_file:
        json.dump(json_data, json_file, indent=4)

    print(const_int_dates)
    # Converti en Princing Input
    past_lines = [pricing_pb2.PastLines(value=row) for row in past]

    return pricing_pb2.PricingInput(
        past=past_lines,
        monitoringDateReached=True,
        time=0,
        json= "AGPS_/AGPS/fichier_in.json"
    )

def main():
    start_date = datetime.datetime(year=2009, month=1, day=5)

    pricing_input = get_pricing_input(start_date)
    
    empty = pricing_pb2.Empty()

    ################## TEST #####################

    # Envoyer la requête au serveur
    response = STUB.PriceAndDeltas(pricing_input)

    # Afficher la réponse
    print(f"✅ Prix estimé : {response.price}")
    print(f"✅ Deltas estimés : {response.deltas}")
    print(f"✅ Écart-type du prix : {response.priceStdDev}")
    print(f"✅ Écart-type des deltas : {response.deltasStdDev}")
    # response = stub.Heartbeat(empty)