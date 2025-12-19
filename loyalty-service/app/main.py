from fastapi import FastAPI
from app.routers.loyalty_router import router

app = FastAPI(
    title="Loyalty Service — Система управления кофейней",
    description="Микросервис программы лояльности",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Loyalty Service работает!"}