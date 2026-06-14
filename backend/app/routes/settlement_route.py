from fastapi import APIRouter
from app.services.balance_service import BalanceService

router = APIRouter()

@router.get("/balances")
def get_balances():
    service = BalanceService()
    return service.compute_balances()

@router.get("/simplified")
def get_simplified_settlement():
    service = BalanceService()
    return service.simplify()
