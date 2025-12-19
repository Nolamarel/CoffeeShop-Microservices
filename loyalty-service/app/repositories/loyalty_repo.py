from uuid import UUID
from app.models.loyalty import LoyaltyAccount

loyalty_db: dict[UUID, LoyaltyAccount] = {}

class LoyaltyRepository:
    def get_or_create(self, customer_id: UUID) -> LoyaltyAccount:
        if customer_id not in loyalty_db:
            loyalty_db[customer_id] = LoyaltyAccount(customer_id=customer_id)
        return loyalty_db[customer_id]

    def accrue_points(self, customer_id: UUID, order_amount: float) -> LoyaltyAccount:
        acc = self.get_or_create(customer_id)
        acc.total_spent += order_amount

        points = int(order_amount * acc.cashback_percent / 100)
        acc.points_balance += points

        self._update_level(acc)
        return acc

    def redeem_points(self, customer_id: UUID, points_to_use: int) -> dict:
        acc = self.get_or_create(customer_id)

        if points_to_use > acc.points_balance:
            raise ValueError("Недостаточно баллов")

        acc.points_balance -= points_to_use

        return {
            "discount": points_to_use,
            "new_balance": acc.points_balance,
            "account": acc
        }

    def _update_level(self, acc: LoyaltyAccount):
        if acc.total_spent >= 50000:
            acc.level = "Gold"; acc.cashback_percent = 15
        elif acc.total_spent >= 20000:
            acc.level = "Silver"; acc.cashback_percent = 10
        else:
            acc.level = "Bronze"; acc.cashback_percent = 5