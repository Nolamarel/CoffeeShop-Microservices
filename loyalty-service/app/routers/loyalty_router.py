from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID
from pydantic import BaseModel, Field
from app.services.loyalty_service import LoyaltyService

router = APIRouter(prefix="/loyalty", tags=["Loyalty"])

CURRENT_USER = UUID("11111111-1111-1111-1111-111111111111")

class RedeemRequest(BaseModel):
    points_to_use: int = Field(..., ge=1)

@router.get("/")
def get_my_loyalty(customer_id: UUID = CURRENT_USER, service: LoyaltyService = Depends()):
    return service.get_account(customer_id)

@router.post("/redeem")
def redeem_points(
    payload: RedeemRequest,
    customer_id: UUID = CURRENT_USER,
    service: LoyaltyService = Depends()
):
    try:
        result = service.redeem_points(customer_id, payload.points_to_use)
        return {
            "message": "Баллы успешно списаны",
            "discount_rub": result["discount"],
            "new_balance_after": result["new_balance"],
            "current_level": result["account"].level,
            "points_left": result["account"].points_balance
        }
    except ValueError as e:
        raise HTTPException(400, str(e))

@router.post("/internal/accrue")
def internal_accrue(customer_id: UUID, order_amount: float):
    service = LoyaltyService()
    account = service.accrue_after_payment(customer_id, order_amount)
    return {"points_added": int(order_amount * account.cashback_percent / 100), "new_balance": account.points_balance}