# review-service/tests/unit/test_review_model.py
import pytest
from uuid import uuid4, UUID
from app.models.review import Review

@pytest.fixture
def valid_customer_id() -> UUID:
    return UUID("11111111-1111-1111-1111-111111111111")

@pytest.fixture
def valid_order_id() -> UUID:
    return uuid4()

def test_review_creation(valid_customer_id, valid_order_id):
    review = Review(
        id=uuid4(),
        order_id=valid_order_id,
        customer_id=valid_customer_id,
        rating=5,
        comment="Вкусный капучино!"
    )
    assert review.rating == 5
    assert review.comment == "Вкусный капучино!"
    assert review.created_at is not None

def test_rating_must_be_between_1_and_5(valid_customer_id, valid_order_id):
    with pytest.raises(ValueError):
        Review(id=uuid4(), order_id=valid_order_id, customer_id=valid_customer_id, rating=0)
    with pytest.raises(ValueError):
        Review(id=uuid4(), order_id=valid_order_id, customer_id=valid_customer_id, rating=6)

def test_rating_can_be_without_comment(valid_customer_id, valid_order_id):
    review = Review(
        id=uuid4(),
        order_id=valid_order_id,
        customer_id=valid_customer_id,
        rating=4
    )
    assert review.comment is None
    assert review.created_at is not None


