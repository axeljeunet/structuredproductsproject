from population.loader import DataLoader
from population.storage import DataStorage
from tests.test_services import test_get_all_prices_by_dates, test_get_prices_by_indexes_and_dates
import pandas as pd
import datetime
import numpy as np
import pricing_pb2
import pricing_pb2_grpc
import json
import os
import grpc

def rebalancingInformation():
    return

def information():
    return

def rebalance():
    return

def main():
    # Charger les données depuis Excel
    file_path = "~/3aif/AGPS/DonneesGPS2025.xlsx"
    market_data = DataLoader.load_from_file(file_path)

    start_date = datetime.datetime(year=2009, month=1, day=5)
    end_date = datetime.datetime(year=2014, month=1, day=6)

    constatation_dates = [datetime.datetime(year=2010, month=1, day=4),
                datetime.datetime(year=2011, month=1, day=4),
                datetime.datetime(year=2012, month=1, day=4),
                datetime.datetime(year=2013, month=1, day=4),
                datetime.datetime(year=2014, month=1, day=6)
                ]

    const_int_dates = [0]  # Début à 0 pour le premier point
    for date in constatation_dates:
        business_days_count = len(pd.bdate_range(start=start_date, end=date)) - 1  # -1 pour exclure start_date
        const_int_dates.append(business_days_count)

    # print(datetime.datetime(year=2006, month=1, day=4) in constatation_dates)
    vols, corr = DataLoader.get_volatility(datetime.datetime(year=2000, month=1, day=3), start_date, market_data)
    print(vols)
    past = DataLoader.get_adjusted_prices(start_date, True, market_data, start_date, constatation_dates, const_int_dates)
    interest_rates = list(market_data.interest_rates.loc[start_date])
    print(interest_rates)

    maturity_in_days = len(pd.bdate_range(start=start_date, end=end_date)) - 1


    json_data = {
        "Interest Rates": interest_rates,
        "Volatilities": vols,
        "Correlations": corr,
        "Constatation Dates": const_int_dates,
        "Maturity": maturity_in_days
    }

    # Convertir ~ en chemin absolu
    json_file_path = os.path.expanduser("~/3aif/AGPS/fichier_in.json")

    # Créer le fichier et écrire les données JSON
    with open(json_file_path, "w") as json_file:
        json.dump(json_data, json_file, indent=4)

    print(const_int_dates)
    # Converti en Princing Input
    past_lines = [pricing_pb2.PastLines(value=row) for row in past]
    pricing_input = pricing_pb2.PricingInput(
        past=past_lines,
        monitoringDateReached=True,
        time=0,
        json= "/home/ensimag/3aif/AGPS/fichier_in.json"
    )
    
    empty = pricing_pb2.Empty()


    ################## TEST #####################
    SERVER_ADDRESS = "localhost:50051"
    with grpc.insecure_channel(SERVER_ADDRESS) as channel:
        stub = pricing_pb2_grpc.GrpcPricerStub(channel)

        # Envoyer la requête au serveur
        response = stub.PriceAndDeltas(pricing_input)

        # Afficher la réponse
        print(f"✅ Prix estimé : {response.price}")
        print(f"✅ Deltas estimés : {response.deltas}")
        print(f"✅ Écart-type du prix : {response.priceStdDev}")
        print(f"✅ Écart-type des deltas : {response.deltasStdDev}")
        # response = stub.Heartbeat(empty)