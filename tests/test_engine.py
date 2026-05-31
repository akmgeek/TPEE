# tests/test_engine.py

import pytest
from unittest.mock import patch, MagicMock
import json
import urllib.request

from backend.engine import (
    haversine_distance,
    geocode_city,
    generate_dynamic_activities,
    score_activities,
    optimize_day_route,
    plan_trip
)

def test_haversine_distance():
    # Coords of Tokyo and Paris
    tokyo = [35.6762, 139.6503]
    paris = [48.8566, 2.3522]
    dist = haversine_distance(tokyo, paris)
    # Distance is roughly 9700-9800 km
    assert 9700 <= dist <= 9800

def test_geocode_city_preset():
    # London is in the offline presets
    res = geocode_city("London")
    assert res is not None
    assert res["name"] == "London"
    assert res["country"] == "United Kingdom"
    assert res["coords"] == [51.5074, -0.1278]

    # Matching with spaces or capitalizations
    res_lower = geocode_city("  london  ")
    assert res_lower is not None
    assert res_lower["name"] == "London"

def test_geocode_city_partial_match():
    # 'london, uk' should partial match 'london'
    res = geocode_city("london, uk")
    assert res is not None
    assert res["name"] == "London"

@patch('urllib.request.urlopen')
def test_geocode_city_online_fallback(mock_urlopen):
    # Mocking Nominatim response for Berlin
    mock_response = MagicMock()
    mock_response.read.return_value = json.dumps([{
        "display_name": "Berlin, Germany",
        "lat": "52.5200",
        "lon": "13.4050"
    }]).encode('utf-8')
    mock_urlopen.return_value.__enter__.return_value = mock_response

    res = geocode_city("Berlin")
    assert res is not None
    assert res["name"] == "Berlin"
    assert res["country"] == "Germany"
    assert res["coords"] == [52.5200, 13.4050]

@patch('urllib.request.urlopen')
def test_geocode_city_not_found(mock_urlopen):
    # Geocoder returns empty array
    mock_response = MagicMock()
    mock_response.read.return_value = json.dumps([]).encode('utf-8')
    mock_urlopen.return_value.__enter__.return_value = mock_response

    res = geocode_city("NonexistentCity12345")
    assert res is None

def test_generate_dynamic_activities():
    coords = [40.7128, -74.0060]
    acts = generate_dynamic_activities("New York", coords)
    assert len(acts) == 10
    for act in acts:
        assert "New York" in act["name"]
        assert len(act["coords"]) == 2
        # Check coordinates are within +/- 0.02 of center
        assert abs(act["coords"][0] - coords[0]) <= 0.025
        assert abs(act["coords"][1] - coords[1]) <= 0.025

def test_score_activities():
    activities = [
        {"id": "a1", "rating": 4.5, "category": "culture", "cost": 0.0, "is_outdoor": True},
        {"id": "a2", "rating": 4.8, "category": "nature", "cost": 50.0, "is_outdoor": True},
        {"id": "a3", "rating": 4.2, "category": "food", "cost": 10.0, "is_outdoor": False},
        {"id": "a4", "rating": 4.0, "category": "relaxation", "cost": 90.0, "is_outdoor": False}
    ]

    # Test preference matching & budget tier constraints
    # 'budget' tier should exclude cost > 30.0 (a2, a4 excluded)
    scored = score_activities(activities, preferences=["culture"], budget_tier="budget", is_rainy=False)
    # Expected: only a1 (cost 0) and a3 (cost 10) are under 30.0.
    assert len(scored) == 2
    assert scored[0]["id"] == "a1" # rating 4.5 + 5 (preference) = 9.5; a3 has score 4.2

    # Test rain penalty for outdoor activities
    # 'mid_range' allows cost up to 70.0 (so a1, a2, a3 are allowed, a4 excluded)
    # Rainy day: outdoor activities (a1, a2) get -15.0 penalty
    scored_rain = score_activities(activities, preferences=["culture", "nature"], budget_tier="mid_range", is_rainy=True)
    # Expected order: a3 (indoor, score 4.2), then a1 (outdoor, penalized), then a2 (outdoor, penalized)
    assert scored_rain[0]["id"] == "a3"

def test_optimize_day_route():
    start = [0.0, 0.0]
    # We place activities at [1.0, 0.0] and [0.1, 0.0]. Nearest neighbor should pick [0.1, 0.0] first.
    activities = [
        {"id": "far", "coords": [1.0, 0.0]},
        {"id": "near", "coords": [0.1, 0.0]}
    ]
    optimized = optimize_day_route(activities, start)
    assert len(optimized) == 2
    assert optimized[0]["id"] == "near"
    assert optimized[1]["id"] == "far"
    assert "distance_from_prev_km" in optimized[0]

def test_plan_trip():
    # Using Tokyo preset (hasHand-curated activities)
    trip = plan_trip(
        destination="Tokyo",
        preferences=["culture", "food"],
        budget_tier="mid_range",
        days=2,
        pace="active" # 2 activities per day
    )

    assert trip["destination"] == "Tokyo"
    assert trip["days"] == 2
    assert trip["pace"] == "active"
    assert len(trip["itinerary"]) == 2
    assert len(trip["itinerary"][0]["schedule"]) == 2
    assert len(trip["itinerary"][1]["schedule"]) == 2
    assert len(trip["all_activities"]) > 0
