
import pytest
from uuid import uuid4, UUID
from app.services.review_service import ReviewService
from app.repositories.review_repo import reviews_db


@pytest.fixture(autouse=True)
def clear_db():
    reviews_db.clear()


@pytest.fixture
def service() -> ReviewService:
    return ReviewService()


def test_create_review_returns_review_with_id(service):
    review = service.create_review(
        order_id=uuid4(),
        customer_id=UUID("11111111-1111-1111-1111-111111111111"),
        rating=5,
        comment="Отлично!"
    )
    assert review.id is not None
    assert review.rating == 5


def test_get_all_reviews_after_creation(service):
    service.create_review(uuid4(), UUID("11111111-1111-1111-1111-111111111111"), 4)
    service.create_review(uuid4(), UUID("22222222-2222-2222-2222-222222222222"), 5)

    reviews = service.get_all_reviews()
    assert len(reviews) == 2