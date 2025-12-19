from fastapi import FastAPI
from app.routers.review_router import router

app = FastAPI(
    title="Review Service — Система управления кофейней",
    description="Микросервис отзывов",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Review Service работает!"}