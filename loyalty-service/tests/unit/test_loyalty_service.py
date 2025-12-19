# import pytest
# from uuid import UUID
# from app.services.loyalty_service import LoyaltyService
#
#
# @pytest.fixture
# def service():
#     return LoyaltyService()
#
#
# def test_accrue_points_calculates_correctly(service):
#     customer_id = UUID("11111111-1111-1111-1111-111111111111")
#
#     acc = service.accrue_after_payment(customer_id, 3000.0)
#     assert acc.points_balance == 150
#     assert acc.total_spent == 3000.0
#     assert acc.level == "Bronze"
#
#     acc = service.accrue_after_payment(customer_id, 22000.0)
#     assert acc.points_balance == 1250
#     assert acc.total_spent == 25000.0
#     assert acc.level == "Silver"
#     assert acc.cashback_percent == 10
#
#
# def test_redeem_points_success(service):
#     customer_id = UUID("11111111-1111-1111-1111-111111111111")
#
#     service.accrue_after_payment(customer_id, 10000.0)
#
#     result = service.redeem_points(customer_id, 300)
#
#     assert result["discount"] == 300
#     assert result["new_balance"] == 1950
#     assert "account" in result
#
# def test_redeem_points_works_even_without_enough_points_check(service):
#     customer_id = UUID("11111111-1111-1111-1111-111111111111")
#
#     result = service.redeem_points(customer_id, 100)
#     assert result["discount"] == 100
#     assert "new_balance" in result