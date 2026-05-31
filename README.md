# WanderSync | Dynamic Travel Planning & Experience Engine

WanderSync is an interactive, high-fidelity single-page web application that serves as a dynamic travel experience engine. It generates day-by-day itineraries matching user travel preferences, budget thresholds, and pace constraints. Additionally, it implements real-time weather disruption handling and automatic route re-sequencing.

---

## ✨ Features

1. **Anywhere Destination Search (Geocoding)**: Type any city worldwide (e.g., *Delhi, Goa, Paris, London, Sydney*). The engine automatically resolves the location's latitude and longitude using OpenStreetMap's Nominatim geocoder.
2. **Procedural Activity Generation**: 
   - Known cities are seeded with hand-curated activities (e.g., Paris, Tokyo, Rome, New York, Reykjavik, Delhi, Goa, Mumbai, Bengaluru, Jaipur).
   - Any unknown/custom city triggers a procedural engine that builds themed, localized activities offset around the resolved coordinates.
3. **Route Optimization**: Itineraries are dynamically sequenced using a **Nearest Neighbor Traveling Salesman Algorithm** from the city center, minimizing transit distances.
4. **Real-time Disruption Simulation**: Toggle sunny ☀️ and rainy 🌧️ weather states per day. Adverse weather triggers a real-time recalculation, replacing outdoor activities with indoor alternatives (e.g., museums, indoor dining) on the fly.
5. **Interactive Mapping & Analytics**:
   - Plots markers, chronological steps, and lines using **Leaflet.js**.
   - Integrates **Chart.js** doughnut charts showing cost category distributions and progress bars tracking budget limits.
6. **Premium Light Glassmorphic Design**: Sleek, professional light-mode SaaS theme featuring high-contrast slate typography, border-based compact activity cards, soft-tint icons, and clear CartoDB Positron maps.

---

## 🛠️ Architecture & Tech Stack

- **Backend**: Python 3.13 + **FastAPI** + **Uvicorn**
- **Frontend**: Single Page Application (Vanilla HTML5 / Custom CSS3 / ES6 Javascript)
- **Mapping Library**: Leaflet.js
- **Chart Library**: Chart.js
- **Icon Library**: FontAwesome 6

---

## 🚀 Setup & Execution

### 1. Installation & Environment Setup
To initialize the virtual environment and install the required dependencies (FastAPI, Uvicorn, Pydantic):
```powershell
# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Install requirements
pip install -r requirements.txt
```

### 2. Run the Server
Run the FastAPI development server:
```powershell
.\venv\Scripts\uvicorn backend.main:app --host 127.0.0.1 --port 8080
```
Open **[http://127.0.0.1:8080](http://127.0.0.1:8080)** in your web browser.

---

## 🔌 API Endpoints

- **`GET /api/destinations`**: Returns supported preset cities and basic metadata (coords, country, description).
- **`POST /api/plan`**: Plans a trip from scratch.
  - *Payload*:
    ```json
    {
      "destination": "Goa",
      "preferences": ["nature", "food"],
      "budget_tier": "mid_range",
      "days": 3,
      "pace": "active",
      "weather_forecast": ["sunny", "sunny", "sunny"]
    }
    ```
- **`POST /api/replan-day`**: Replans a single day's events (due to weather changes) while preserving activities on other days.
  - *Payload*:
    ```json
    {
      "destination": "Goa",
      "preferences": ["nature", "food"],
      "budget_tier": "mid_range",
      "pace": "active",
      "day_num": 2,
      "weather": "rainy",
      "currently_scheduled_ids": ["goa_dudhsagar"],
      "all_other_used_ids": ["goa_cruise", "goa_spice_farm"]
    }
    ```

## ☁️ Vercel Deployment

WanderSync is configured for zero-config serverless deployments on **Vercel**:

1. Install the Vercel CLI (optional):
   ```bash
   npm install -g vercel
   ```
2. Deploy the project from the root folder:
   ```bash
   vercel
   ```
3. Follow the CLI prompt instructions. Vercel will automatically:
   - Read `vercel.json` and configure URL rewrites.
   - Detect the Python runtime via `requirements.txt`.
   - Mount `api/index.py` as a serverless ASGI function mapping the `/api/*` endpoints.
   - Serve the assets in the `/static` folder directly via its Global Edge Network.
