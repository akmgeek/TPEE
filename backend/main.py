# backend/main.py

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional

from backend.data import DESTINATIONS
from backend.engine import plan_trip, score_activities, optimize_day_route, geocode_city, generate_dynamic_activities


app = FastAPI(
    title="Travel Planning and Experience Engine API",
    description="API for dynamically planning trips and handling real-time routing constraints",
    version="1.0.0"
)

# Enable CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Pydantic Schemas ---

class PlanRequest(BaseModel):
    destination: str = Field(..., example="Tokyo")
    preferences: List[str] = Field(default_factory=list, example=["culture", "food"])
    budget_tier: str = Field(..., example="mid_range") # budget, mid_range, luxury
    days: int = Field(..., ge=1, le=10, example=3)
    pace: str = Field(..., example="active") # relaxed, active, packed
    weather_forecast: Optional[List[str]] = Field(default=None, example=["sunny", "sunny", "rainy"])

class ReplanDayRequest(BaseModel):
    destination: str
    preferences: List[str]
    budget_tier: str
    pace: str
    day_num: int
    weather: str
    currently_scheduled_ids: List[str]
    all_other_used_ids: List[str]

# --- API Routes ---

@app.get("/api/destinations")
def get_destinations():
    """
    Returns a list of supported destinations and basic metadata.
    """
    result = []
    for key, val in DESTINATIONS.items():
        result.append({
            "id": key,
            "name": val["name"],
            "country": val["country"],
            "description": val["description"],
            "coords": val["coords"],
            "activity_count": len(val["activities"])
        })
    return result

@app.post("/api/plan")
def create_itinerary(req: PlanRequest):
    """
    Generates a full trip plan based on preferences, pace, and weather.
    Supports preset destinations AND arbitrary dynamic destinations using geocoding.
    """
    try:
        itinerary = plan_trip(
            destination=req.destination,
            preferences=req.preferences,
            budget_tier=req.budget_tier,
            days=req.days,
            pace=req.pace,
            weather_forecast=req.weather_forecast
        )
        return itinerary
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/replan-day")
def replan_day(req: ReplanDayRequest):
    """
    Replans a single day's activities due to weather changes,
    ensuring activities scheduled on OTHER days are not stolen.
    Supports preset destinations AND arbitrary dynamic destinations.
    """
    destination_key = req.destination.strip()
    
    # Check if preset
    preset_key = None
    for k in DESTINATIONS.keys():
        if k.lower() == destination_key.lower():
            preset_key = k
            break
            
    if preset_key:
        city_data = DESTINATIONS[preset_key]
        city_coords = city_data["coords"]
        all_activities = city_data["activities"]
    else:
        # Dynamic fallback
        geo = geocode_city(destination_key)
        if not geo:
            city_coords = [28.6139, 77.2090]
            resolved_name = destination_key
        else:
            city_coords = geo["coords"]
            resolved_name = geo["name"]
        all_activities = generate_dynamic_activities(resolved_name, city_coords)
    
    # Determine how many activities we need
    if req.pace == "relaxed":
        acts_count = 1
    elif req.pace == "active":
        acts_count = 2
    else:
        acts_count = 3
        
    # The pool of selectable activities
    selectable = [
        act for act in all_activities
        if act["id"] not in req.all_other_used_ids
    ]
    
    # Score activities based on the new weather condition for this day
    is_rainy = req.weather == "rainy"
    scored = score_activities(selectable, req.preferences, req.budget_tier, is_rainy)
    
    # Take top N
    selected_acts = scored[:acts_count]
    
    # Fill with fallback if we are short
    if len(selected_acts) < acts_count:
        already_picked = [a["id"] for a in selected_acts]
        fallback_pool = [
            act for act in all_activities
            if act["id"] not in req.all_other_used_ids and act["id"] not in already_picked
        ]
        fallback_pool.sort(key=lambda x: x["rating"], reverse=True)
        selected_acts.extend(fallback_pool[:(acts_count - len(selected_acts))])
        
    # Optimize sequence
    optimized_acts = optimize_day_route(selected_acts, city_coords)
    
    # Structure slots
    slots = ["Morning", "Afternoon", "Evening"]
    day_slots = []
    
    for idx, act in enumerate(optimized_acts):
        slot_name = slots[idx] if idx < len(slots) else f"Extra {idx-1}"
        day_slots.append({
            "time_slot": slot_name,
            "activity": act
        })
        
    return {
        "day": req.day_num,
        "weather": req.weather,
        "schedule": day_slots
    }


# Mount frontend files (index.html, styles, javascript)
app.mount("/", StaticFiles(directory="static", html=True), name="static")
