from fastapi import APIRouter
import controller 

router = APIRouter()

@router.get("/rebalancingInformation")
def rebalancingInformation():
    return controller.rebalancingInformation()

@router.get("/information")
def information():
    return controller.information()

@router.post("/rebalance")
def rebalance():
    return controller.rebalance()