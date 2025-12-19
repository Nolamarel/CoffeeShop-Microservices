# # loyalty-service/tests/integrations/test_loyalty_integration.py
#
# # loyalty-service/tests/integrations/test_loyalty_integration.py
#
# import pytest
# from uuid import UUID
# from app.repositories.loyalty_repo import LoyaltyRepository, loyalty_db
# from app.models.loyalty import LoyaltyAccount
#
#
# @pytest.fixture(autouse=True)
# def clear_db():
#     loyalty_db.clear()  # очищаем настоящую базу перед каждым тестом
#
#
# def test_full_loyalty_flow_with_real_repository():
#     """Проверка полного цикла работы с реальной in-memory базой"""
#     repo = LoyaltyRepository()
#     customer_id = UUID("11111111-1111-1111-1111-111111111111")
#
#     # 1. Первый заказ — 3000 → Bronze, 5%, 150 баллов
#     acc1 = repo.accrue_points(customer_id, 3000.0)
#     assert acc1.level == "Bronze"
#     assert acc1.cashback_percent == 5
#     assert acc1.points_balance == 150
#     assert acc1.total_spent == 3000.0
#
#     # Проверяем, что данные реально в базе
#     assert customer_id in loyalty_db
#     assert loyalty_db[customer_id].total_spent == 3000.0
#
#     # 2. Большой заказ — переходим на Silver (≥20000)
#     acc2 = repo.accrue_points(customer_id, 22000.0)
#     assert acc2.level == "Silver"
#     assert acc2.cashback_percent == 10
#     assert acc2.total_spent == 25000.0
#     # 22000 * 10% = 2200 баллов + 150 = 2350
#     assert acc2.points_balance == 2350
#
#     # 3. Списываем 500 баллов
#     result = repo.redeem_points(customer_id, 500)
#     assert result["discount"] == 500
#     assert result["new_balance"] == 1850  # 2350 - 500
#     assert result["account"].points_balance == 1850
#
#     # 4. Проверяем, что база обновилась
#     final_acc = loyalty_db[customer_id]
#     assert final_acc.points_balance == 1850
#     assert final_acc.total_spent == 25000.0  # сумма покупок не меняется
#     assert final_acc.level == "Silver"
#
#     # 5. Ещё один заказ — проверяем, что кэшбек уже 10%
#     acc3 = repo.accrue_points(customer_id, 10000.0)
#     added_points = 10000 * 0.10  # 10% от 10000
#     assert acc3.points_balance == 1850 + 1000  # 2850