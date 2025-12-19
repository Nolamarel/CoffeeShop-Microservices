# review-service/tests/component/test_review_api_component.py

from fastapi.testclient import TestClient
from uuid import uuid4, UUID
from app.main import app
import pytest

client = TestClient(app)


def test_full_review_api_component_flow():
    customer_id = "11111111-1111-1111-1111-111111111111"
    order_id_1 = str(uuid4())
    order_id_2 = str(uuid4())

    response = client.post("/reviews/", json={
        "order_id": order_id_1,
        "customer_id": customer_id,
        "rating": 5,
        "comment": "Самый вкусный капучино в мире!"
    })
    assert response.status_code == 201
    review1 = response.json()
    assert review1["rating"] == 5
    assert review1["id"] is not None

    response = client.post("/reviews/", json={
        "order_id": order_id_2,
        "customer_id": "22222222-2222-2222-2222-222222222222",
        "rating": 4,
        "comment": "Хорошо, но можно лучше"
    })
    assert response.status_code == 201

    response = client.get("/reviews/")
    assert response.status_code == 200
    reviews = response.json()
    assert len(reviews) == 2

    response = client.post("/reviews/", json={
        "order_id": str(uuid4()),
        "customer_id": customer_id,
        "rating": 999,
        "comment": "Слишком круто"
    })
    assert response.status_code == 422