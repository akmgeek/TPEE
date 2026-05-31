# backend/engine.py

import math
import urllib.request
import urllib.parse
import json
import random
from typing import List, Dict, Any, Optional
from backend.data import DESTINATIONS


def haversine_distance(coord1: List[float], coord2: List[float]) -> float:
    """
    Calculate the great-circle distance between two points on the Earth in kilometers.
    """
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    
    R = 6371.0 # Earth radius in km
    
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    
    a = math.sin(dlat / 2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    return R * c

OFFLINE_CITIES = {
    "london": {"name": "London", "country": "United Kingdom", "coords": [51.5074, -0.1278]},
    "sydney": {"name": "Sydney", "country": "Australia", "coords": [-33.8688, 151.2093]},
    "cairo": {"name": "Cairo", "country": "Egypt", "coords": [30.0444, 31.2357]},
    "mumbai": {"name": "Mumbai", "country": "India", "coords": [19.0760, 72.8777]},
    "cape town": {"name": "Cape Town", "country": "South Africa", "coords": [-33.9249, 18.4241]},
    "rio de janeiro": {"name": "Rio de Janeiro", "country": "Brazil", "coords": [-22.9068, -43.1729]},
    "dubai": {"name": "Dubai", "country": "United Arab Emirates", "coords": [25.2048, 55.2708]},
    "tokyo": {"name": "Tokyo", "country": "Japan", "coords": [35.6762, 139.6503]},
    "paris": {"name": "Paris", "country": "France", "coords": [48.8566, 2.3522]},
    "new york": {"name": "New York", "country": "United States", "coords": [40.7128, -74.0060]},
    "rome": {"name": "Rome", "country": "Italy", "coords": [41.9028, 12.4964]},
    "delhi": {"name": "Delhi", "country": "India", "coords": [28.6139, 77.2090]},
    "goa": {"name": "Goa", "country": "India", "coords": [15.4909, 73.8278]}
}

def geocode_city(city_name: str) -> Optional[Dict[str, Any]]:
    """
    Geocodes a city name, using a fast local offline dictionary fallback
    and falling back to OpenStreetMap's Nominatim API if not found.
    """
    clean_name = city_name.strip().lower()
    if not clean_name:
        return None
        
    # 1. Check exact match in offline dictionary
    if clean_name in OFFLINE_CITIES:
        data = OFFLINE_CITIES[clean_name]
        return {
            "name": data["name"],
            "country": data["country"],
            "coords": data["coords"]
        }
        
    # 2. Check partial matches (e.g., 'london, uk' -> 'london')
    for key, data in OFFLINE_CITIES.items():
        if key in clean_name or clean_name in key:
            return {
                "name": data["name"],
                "country": data["country"],
                "coords": data["coords"]
            }
            
    # 3. Fallback to Nominatim geocoder
    try:
        quoted_city = urllib.parse.quote(city_name)
        url = f"https://nominatim.openstreetmap.org/search?q={quoted_city}&format=json&limit=1"
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'WanderSyncTravelPlanner/1.0 (amit.projects@tpee)'}
        )
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode())
            if data:
                item = data[0]
                display_name = item.get("display_name", city_name)
                parts = display_name.split(",")
                country = parts[-1].strip() if parts else "Unknown"
                return {
                    "name": parts[0].strip() if parts else city_name,
                    "country": country,
                    "coords": [float(item["lat"]), float(item["lon"])]
                }
    except Exception as e:
        print(f"Geocoding error for '{city_name}': {e}")
    return None

def generate_dynamic_activities(city_name: str, coords: List[float]) -> List[Dict[str, Any]]:
    """
    Procedurally generates 10 themed activities around a city's center coordinates.
    Adds small random offsets to coordinates so they appear distributed on the map.
    """
    lat, lng = coords
    
    templates = [
        {
            "id_suffix": "heritage_fort",
            "name_template": "{city} Heritage Fort & Palace Ruins",
            "description_template": "Explore the majestic architectural ruins, fortification walls, and historical exhibits of {city}.",
            "category": "culture",
            "cost": 10.0,
            "duration_hours": 2.5,
            "is_outdoor": True,
            "rating": 4.6
        },
        {
            "id_suffix": "botanical_garden",
            "name_template": "{city} Royal Botanical Gardens",
            "description_template": "Take a tranquil stroll among exotic plants, water lilies, and historic trees in this central green park.",
            "category": "nature",
            "cost": 2.0,
            "duration_hours": 2.0,
            "is_outdoor": True,
            "rating": 4.5
        },
        {
            "id_suffix": "central_museum",
            "name_template": "{city} Historical & Art Museum",
            "description_template": "Browse prehistoric artifacts, local artisan crafts, and royal portraits inside a beautiful climate-controlled gallery.",
            "category": "culture",
            "cost": 5.0,
            "duration_hours": 3.0,
            "is_outdoor": False,
            "rating": 4.7
        },
        {
            "id_suffix": "street_food_crawl",
            "name_template": "{city} Downtown Street Food Crawl",
            "description_template": "Savor {city}'s famous local delicacies, spicy street snacks, and sweet desserts guided by a culinary expert.",
            "category": "food",
            "cost": 15.0,
            "duration_hours": 2.0,
            "is_outdoor": True,
            "rating": 4.8
        },
        {
            "id_suffix": "hill_sunset_trek",
            "name_template": "{city} Clifftop Sunset Trek",
            "description_template": "A moderately active hike leading to a panoramic overlook point of {city} and surrounding valleys.",
            "category": "adventure",
            "cost": 0.0,
            "duration_hours": 3.0,
            "is_outdoor": True,
            "rating": 4.7
        },
        {
            "id_suffix": "wellness_spa",
            "name_template": "{city} Geothermal Spa & Wellness Center",
            "description_template": "Unwind with healing hot spring pools, steam baths, and organic herbal massages.",
            "category": "relaxation",
            "cost": 40.0,
            "duration_hours": 2.5,
            "is_outdoor": False,
            "rating": 4.6
        },
        {
            "id_suffix": "water_kayaking",
            "name_template": "{city} Riverfront Kayaking & Adventure",
            "description_template": "Paddle down {city}'s scenic riverways, passing historical bridges and observing wildlife.",
            "category": "adventure",
            "cost": 20.0,
            "duration_hours": 2.0,
            "is_outdoor": True,
            "rating": 4.5
        },
        {
            "id_suffix": "old_town_walk",
            "name_template": "{city} Old Town Heritage Street Walk",
            "description_template": "Walk past ancient markets, colonial arches, and centuries-old storefronts in the old city quarter.",
            "category": "culture",
            "cost": 0.0,
            "duration_hours": 1.5,
            "is_outdoor": True,
            "rating": 4.6
        },
        {
            "id_suffix": "lake_boating",
            "name_template": "{city} Scenic Lake Boating Tour",
            "description_template": "Enjoy a peaceful rowboat or motorboat tour of the city's central lake with bird-watching.",
            "category": "relaxation",
            "cost": 8.0,
            "duration_hours": 1.5,
            "is_outdoor": True,
            "rating": 4.5
        },
        {
            "id_suffix": "rooftop_bistro",
            "name_template": "{city} Rooftop Bistro & Live Music",
            "description_template": "Sample gourmet local dishes and sip signature beverages with sweeping skyline views.",
            "category": "food",
            "cost": 30.0,
            "duration_hours": 2.0,
            "is_outdoor": False,
            "rating": 4.8
        }
    ]
    
    generated = []
    rng = random.Random(city_name.lower())
    
    for tpl in templates:
        offset_lat = rng.uniform(-0.02, 0.02)
        offset_lng = rng.uniform(-0.02, 0.02)
        
        act = {
            "id": f"dyn_{city_name.lower().replace(' ', '_')}_{tpl['id_suffix']}",
            "name": tpl["name_template"].format(city=city_name),
            "description": tpl["description_template"].format(city=city_name),
            "category": tpl["category"],
            "cost": tpl["cost"],
            "duration_hours": tpl["duration_hours"],
            "coords": [round(lat + offset_lat, 5), round(lng + offset_lng, 5)],
            "is_outdoor": tpl["is_outdoor"],
            "rating": tpl["rating"]
        }
        generated.append(act)
        
    return generated

def score_activities(

    activities: List[Dict[str, Any]],
    preferences: List[str],
    budget_tier: str,
    is_rainy: bool
) -> List[Dict[str, Any]]:
    """
    Scores and filters activities based on user preferences, budget, and weather conditions.
    """
    scored_list = []
    
    for act in activities:
        # Base score starts with the rating
        score = act["rating"]
        
        # Preference category match
        if act["category"].lower() in [p.lower() for p in preferences]:
            score += 5.0
            
        # Budget constraint filters
        cost = act["cost"]
        if budget_tier == "budget":
            if cost == 0.0:
                score += 3.0
            elif cost > 30.0:
                # Exclude high cost activities for budget tier
                continue
        elif budget_tier == "mid_range":
            if cost > 70.0:
                # Exclude ultra-luxury activities
                continue
            elif cost > 30.0:
                score -= 1.0 # Slight penalty for upper-mid costs
        else: # luxury
            if cost > 50.0:
                score += 2.0 # Prefer premium experiences in luxury mode
                
        # Weather constraint logic
        if is_rainy and act["is_outdoor"]:
            # Drastically reduce score for outdoor activities when it is raining
            score -= 15.0
        elif not is_rainy and not act["is_outdoor"]:
            # Slight boost to outdoor activities when it is sunny
            score += 0.5
            
        scored_list.append({
            "activity": act,
            "score": score
        })
        
    # Sort by score descending
    scored_list.sort(key=lambda x: x["score"], reverse=True)
    return [item["activity"] for item in scored_list]

def optimize_day_route(activities: List[Dict[str, Any]], start_coords: List[float]) -> List[Dict[str, Any]]:
    """
    Optimizes the order of activities for a single day using Nearest Neighbor algorithm
    starting from a center coordinate (e.g. city center or hotel).
    """
    if not activities:
        return []
        
    optimized = []
    current_coords = start_coords
    remaining = list(activities)
    
    while remaining:
        # Find closest activity to current coordinates
        closest_idx = 0
        min_dist = float('inf')
        
        for idx, act in enumerate(remaining):
            dist = haversine_distance(current_coords, act["coords"])
            if dist < min_dist:
                min_dist = dist
                closest_idx = idx
                
        closest_act = remaining.pop(closest_idx)
        # Store computed distance from previous stop
        closest_act_copy = dict(closest_act)
        closest_act_copy["distance_from_prev_km"] = round(min_dist, 2)
        
        optimized.append(closest_act_copy)
        current_coords = closest_act["coords"]
        
    return optimized

def plan_trip(
    destination: str,
    preferences: List[str],
    budget_tier: str,
    days: int,
    pace: str,
    weather_forecast: Optional[List[str]] = None
) -> Dict[str, Any]:
    """
    Generates a full day-by-day optimized itinerary based on constraints.
    Supports preset destinations AND arbitrary dynamic destinations using geocoding.
    """
    destination_key = destination.strip()
    
    # Check if it matches preset keys exactly (case insensitive)
    preset_key = None
    for k in DESTINATIONS.keys():
        if k.lower() == destination_key.lower():
            preset_key = k
            break
            
    if preset_key:
        city_data = DESTINATIONS[preset_key]
        city_coords = city_data["coords"]
        all_activities = city_data["activities"]
        country = city_data["country"]
        description = city_data["description"]
        resolved_name = city_data["name"]
    else:
        # Dynamic Geocoding fallback
        geo = geocode_city(destination_key)
        if not geo:
            # Default to New Delhi coordinates as fallback
            resolved_name = destination_key
            country = "India (Default Coordinates)"
            city_coords = [28.6139, 77.2090]
            description = f"Procedurally generated travel itinerary for {resolved_name}."
        else:
            resolved_name = geo["name"]
            country = geo["country"]
            city_coords = geo["coords"]
            description = f"Procedurally generated travel itinerary for {resolved_name}, geocoded in {country}."
            
        all_activities = generate_dynamic_activities(resolved_name, city_coords)
    
    # Initialize weather if none provided
    if not weather_forecast or len(weather_forecast) < days:
        weather_forecast = ["sunny"] * days
        
    # Determine activities per day based on pace
    if pace == "relaxed":
        acts_per_day = 1
    elif pace == "active":
        acts_per_day = 2
    else: # packed
        acts_per_day = 3
        
    used_activity_ids = set()
    itinerary = []
    total_cost = 0.0
    
    for d in range(days):
        day_num = d + 1
        weather = weather_forecast[d]
        is_rainy = weather == "rainy"
        
        # Get activities scored for this specific day's weather
        available_scored = score_activities(
            [a for a in all_activities if a["id"] not in used_activity_ids],
            preferences,
            budget_tier,
            is_rainy
        )
        
        # Pick the top N activities
        day_activities = available_scored[:acts_per_day]
        
        # If we ran out of activities, we might have to reuse or pick from the main pool
        if len(day_activities) < acts_per_day:
            remaining_needed = acts_per_day - len(day_activities)
            fallback_pool = [
                a for a in all_activities 
                if a["id"] not in [da["id"] for da in day_activities]
            ]
            fallback_scored = score_activities(fallback_pool, preferences, budget_tier, is_rainy)
            day_activities.extend(fallback_scored[:remaining_needed])
            
        # Optimize sequence of these day activities
        optimized_day_acts = optimize_day_route(day_activities, city_coords)
        
        # Build structure for morning/afternoon/evening slots
        slots = ["Morning", "Afternoon", "Evening"]
        day_slots = []
        
        for idx, act in enumerate(optimized_day_acts):
            slot_name = slots[idx] if idx < len(slots) else f"Extra {idx-1}"
            
            # Record used activity so we avoid duplicate scheduling across different days
            used_activity_ids.add(act["id"])
            total_cost += act["cost"]
            
            day_slots.append({
                "time_slot": slot_name,
                "activity": act
            })
            
        itinerary.append({
            "day": day_num,
            "weather": weather,
            "schedule": day_slots
        })
        
    return {
        "destination": resolved_name,
        "country": country,
        "description": description,
        "coords": city_coords,
        "days": days,
        "pace": pace,
        "budget_tier": budget_tier,
        "total_cost": round(total_cost, 2),
        "itinerary": itinerary,
        "all_activities": all_activities
    }
