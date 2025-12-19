from uuid import UUID
from pydantic import BaseModel, ConfigDict

class LoyaltyAccount(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    customer_id: UUID
    level: str = "Bronze"
    points_balance: int = 0
    total_spent: float = 0.0
    cashback_percent: int = 5





