from fastapi import APIRouter
import controller 
from dto.date_request import DateRequest

router = APIRouter()

@router.post("/rebalancingInformation")
def rebalancing_information(data: DateRequest):
    print(f"Getting rebalancing information from date : {data.date}")
    return controller.rebalancing_information(data.date)

@router.post("/information")
def information(data: DateRequest):
    print(f"Getting information from date : {data.date}")
    return controller.information(data.date)

@router.post("/rebalance")
def rebalance(data: DateRequest):
    print(f"Rebalancing portfolio from date : {data.date}")
    return controller.rebalance(data.date)