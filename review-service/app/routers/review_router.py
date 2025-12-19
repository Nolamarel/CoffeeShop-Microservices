from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID
from pydantic import BaseModel, Field
from app.services.review_service import ReviewService

router = APIRouter(prefix="/reviews", tags=["Reviews"])

class ReviewCreateSchema(BaseModel):
    order_id: UUID
    rating: int = Field(ge=1, le=5)
    comment: str | None = None

CURRENT_USER_ID = UUID("11111111-1111-1111-1111-111111111111")

@router.post("/", status_code=201)
async def create_review(payload: ReviewCreateSchema, service: ReviewService = Depends()):
    return service.create_review(
        order_id=payload.order_id,
        customer_id=CURRENT_USER_ID,
        rating=payload.rating,
        comment=payload.comment
    )

@router.get("/{review_id}")
async def get_review(review_id: UUID, service: ReviewService = Depends()):
    try:
        return service.get_review(review_id)
    except KeyError:
        raise HTTPException(404, "Отзыв не найден")

@router.get("/")
async def get_all_reviews(service: ReviewService = Depends()):
    return service.get_all_reviews()