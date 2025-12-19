from uuid import UUID
from app.repositories.review_repo import ReviewRepository

class ReviewService:
    def __init__(self):
        self.repo = ReviewRepository()

    def create_review(self, order_id: UUID, customer_id: UUID, rating: int, comment: str | None = None):
        return self.repo.create(order_id, customer_id, rating, comment)

    def get_review(self, review_id: UUID):
        return self.repo.get_by_id(review_id)

    def get_all_reviews(self):
        return self.repo.get_all()