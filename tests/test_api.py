# tests/test_api.py

import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_api_destinations():
    response = client.get("/api/destinations")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    # Check that preset destinations contain basic fields
    for city in data:
        assert "name" in city
        assert "country" in city
        assert "coords" in city
        assert "activity_count" in city

def test_api_plan():
    payload = {
        "destination": "Goa",
        "preferences": ["nature", "food"],
        "budget_tier": "mid_range",
        "days": 2,
        "pace": "active",
        "weather_forecast": ["sunny", "sunny"]
    }
    response = client.post("/api/plan", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["destination"] == "Goa"
    assert data["days"] == 2
    assert len(data["itinerary"]) == 2
    assert "all_activities" in data

def test_api_replan_day():
    payload = {
        "destination": "Paris",
        "preferences": ["culture"],
        "budget_tier": "luxury",
        "pace": "packed",
        "day_num": 1,
        "weather": "rainy",
        "currently_scheduled_ids": [],
        "all_other_used_ids": []
    }
    response = client.post("/api/replan-day", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["day"] == 1
    assert data["weather"] == "rainy"
    assert "schedule" in data
