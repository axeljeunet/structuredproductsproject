#include <iostream>
#include <memory>
#include <string>
#include <grpcpp/grpcpp.h>
#include "pricing.pb.h"
#include "pricing.grpc.pb.h"

using grpc::Server;
using grpc::ServerBuilder;
using grpc::ServerContext;
using grpc::Status;
using namespace GrpcPricing::Protos;

class GrpcPricerServiceImpl final : public GrpcPricer::Service {
public:
    Status PriceAndDeltas(ServerContext* context, const PricingInput* request, PricingOutput* response) override {
        std::cout << "Received pricing request at time: " << request->time() << std::endl;

        // Simulation de la logique de pricing
        response->set_price(101.5);
        response->add_deltas(0.2);
        response->add_deltas(-0.1);
        response->set_pricestddev(0.05);
        response->add_deltasstddev(0.02);

        return Status::OK;
    }

    Status Heartbeat(ServerContext* context, const Empty* request, ReqInfo* response) override {
        std::cout << "Received heartbeat request" << std::endl;
        response->set_domesticinterestrate(0.03);
        response->set_relativefinitedifferencestep(0.001);
        response->set_samplenb(10000);

        return Status::OK;
    }
};

void RunServer() {
    std::string server_address("0.0.0.0:50051");
    GrpcPricerServiceImpl service;

    ServerBuilder builder;
    builder.AddListeningPort(server_address, grpc::InsecureServerCredentials());
    builder.RegisterService(&service);

    std::unique_ptr<Server> server(builder.BuildAndStart());
    std::cout << "Server listening on " << server_address << std::endl;
    server->Wait();
}

int main() {
    RunServer();
    return 0;
}
