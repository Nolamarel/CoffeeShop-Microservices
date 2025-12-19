from uuid import UUID
from app.repositories.loyalty_repo import LoyaltyRepository

class LoyaltyService:
    def __init__(self):
        self.repo = LoyaltyRepository()

    def get_account(self, customer_id: UUID):
        return self.repo.get_or_create(customer_id)

    def redeem_points(self, customer_id: UUID, points_to_use: int) -> dict:
        result = self.repo.redeem_points(customer_id, points_to_use)

        return {
            "discount": result["discount"],
            "new_balance": result["new_balance"],
            "account": result["account"]
        }

    def accrue_after_payment(self, customer_id: UUID, order_amount: float):
        return self.repo.accrue_points(customer_id, order_amount)


