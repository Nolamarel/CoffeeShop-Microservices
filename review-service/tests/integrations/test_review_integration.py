# tests/integrations/test_review_integration.py

import pytest
from uuid import uuid4, UUID
from app.services.review_service import ReviewService
from app.repositories.review_repo import reviews_db


@pytest.fixture(autouse=True)
def clear_db():
    reviews_db.clear()


def test_full_review_lifecycle_integration():
    service = ReviewService()
    customer_id = UUID("11111111-1111-1111-1111-111111111111")
    order_id = uuid4()

    # Создаём отзыв
    review = service.create_review(
        order_id=order_id,
        customer_id=customer_id,
        rating=5,
        comment="Лучший капучино в городе!"
    )

    assert review.id is not None
    assert review.rating == 5
    assert review.comment == "Лучший капучино в городе!"

    # Проверяем, что он реально сохранился в список
    assert len(reviews_db) == 1
    saved_review = reviews_db[0]
    assert saved_review.id == review.id
    assert saved_review.rating == 5

    # Получаем все отзывы
    all_reviews = service.get_all_reviews()
    assert len(all_reviews) == 1
    assert all_reviews[0].comment == "Лучший капучино в городе!"