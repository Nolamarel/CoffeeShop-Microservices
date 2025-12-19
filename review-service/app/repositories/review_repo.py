from uuid import uuid4, UUID
from datetime import datetime
from app.models.review import Review
from datetime import datetime, timezone

reviews_db: list[Review] = []

class ReviewRepository:
    def create(self, order_id: UUID, customer_id: UUID, rating: int, comment: str | None) -> Review:
        review = Review(
            id=uuid4(),
            order_id=order_id,
            customer_id=customer_id,
            rating=rating,
            comment=comment,
            created_at=datetime.now(timezone.utc)
        )
        reviews_db.append(review)
        return review

    def get_by_id(self, review_id: UUID) -> Review:
        for r in reviews_db:
            if r.id == review_id:
                return r
        raise KeyError("Review not found")

    def get_all(self):
        return reviews_db