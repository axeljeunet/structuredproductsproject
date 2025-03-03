import grpc
import pricing_pb2
import pricing_pb2_grpc

def run():
    # Connexion au serveur C++ qui tourne sur localhost:50051
    channel = grpc.insecure_channel('localhost:50051')
    stub = pricing_pb2_grpc.GrpcPricerStub(channel)

    # Envoi d'une requête de pricing
    past_data = [pricing_pb2.PastLines(value=[1.2, 2.3, 3.4])]
    request = pricing_pb2.PricingInput(
        past=past_data,
        monitoringDateReached=True,
        time=1.0,
        json="{}"
    )

    response = stub.PriceAndDeltas(request)
    print(f"Price: {response.price}")
    print(f"Deltas: {list(response.deltas)}")
    print(f"Price StdDev: {response.priceStdDev}")
    print(f"Deltas StdDev: {list(response.deltasStdDev)}")

    # Envoi d'une requête de Heartbeat
    heartbeat_response = stub.Heartbeat(pricing_pb2.Empty())
    print(f"Domestic Interest Rate: {heartbeat_response.domesticInterestRate}")
    print(f"Finite Difference Step: {heartbeat_response.relativeFiniteDifferenceStep}")
    print(f"Sample Nb: {heartbeat_response.sampleNb}")

if __name__ == '__main__':
    run()
