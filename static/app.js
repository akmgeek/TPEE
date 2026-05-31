// static/app.js

// Global state
let currentTrip = null;
let activeDayIndex = 0;
let map = null;
let mapMarkers = [];
let routePolyline = null;
let budgetChart = null;

// Initializations on page load
document.addEventListener("DOMContentLoaded", () => {
    initMap();
    loadDestinations();
    setupEventListeners();
});

// Initialize Leaflet Map
function initMap() {
    // Default coordinates (centered at Atlantic Ocean)
    map = L.map("map-container", {
        zoomControl: true,
        scrollWheelZoom: true
    }).setView([30, -30], 2);

    // Standard OpenStreetMap tiles
    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
        maxZoom: 19,
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);
}

let presetCities = [];

// Fetch available destinations from API
async function loadDestinations() {
    try {
        const response = await fetch("/api/destinations");
        if (!response.ok) throw new Error("Failed to load destinations");
        presetCities = await response.json();
        setupAutocomplete();
    } catch (err) {
        console.error("Error loading destinations:", err);
        showNotification("error", "Error connecting to backend API. Please make sure the server is running.");
    }
}

// Implement text autocomplete and suggestions selection
function setupAutocomplete() {
    const input = document.getElementById("destination-input");
    const popup = document.getElementById("suggestions-popup");
    
    input.addEventListener("input", () => {
        const val = input.value.trim();
        if (!val) {
            popup.style.display = "none";
            return;
        }
        
        // Filter presets
        const matches = presetCities.filter(city => 
            city.name.toLowerCase().includes(val.toLowerCase()) || 
            city.country.toLowerCase().includes(val.toLowerCase())
        );
        
        popup.innerHTML = "";
        
        // Show matching presets
        matches.forEach(city => {
            const item = document.createElement("div");
            item.className = "suggestions-item";
            item.innerHTML = `
                <span><strong>${city.name}</strong>, ${city.country}</span>
                <span class="country-tag">Preset</span>
            `;
            item.addEventListener("click", () => {
                input.value = city.name;
                popup.style.display = "none";
            });
            popup.appendChild(item);
        });
        
        // Add dynamic fallback search option
        const fallback = document.createElement("div");
        fallback.className = "suggestions-item";
        fallback.innerHTML = `
            <span><i class="fa-solid fa-earth-asia"></i> Search globally for <strong>"${val}"</strong>...</span>
            <span class="country-tag" style="background: rgba(20, 184, 166, 0.15); color: #2dd4bf;">OSM</span>
        `;
        fallback.addEventListener("click", () => {
            input.value = val;
            popup.style.display = "none";
        });
        popup.appendChild(fallback);
        
        popup.style.display = "block";
    });
    
    // Hide popup when clicking outside
    document.addEventListener("click", (e) => {
        if (!input.contains(e.target) && !popup.contains(e.target)) {
            popup.style.display = "none";
        }
    });
}

// Setup all DOM Event Listeners
function setupEventListeners() {
    const form = document.getElementById("planner-form");
    const daysInput = document.getElementById("days");
    const daysVal = document.getElementById("days-val");

    // Sync days slider value
    daysInput.addEventListener("input", (e) => {
        daysVal.textContent = `${e.target.value} Day${e.target.value > 1 ? 's' : ''}`;
    });

    // Handle Form Submit (Plan Trip)
    form.addEventListener("submit", async (e) => {
        e.preventDefault();
        
        const destination = document.getElementById("destination-input").value.trim();
        const days = parseInt(daysInput.value, 10);
        const budget_tier = document.querySelector('input[name="budget"]:checked').value;
        const pace = document.querySelector('input[name="pace"]:checked').value;
        
        if (!destination) {
            showNotification("warn", "Please enter a destination.");
            return;
        }

        // Collect checked preferences
        const preferences = [];
        document.querySelectorAll('input[name="preferences"]:checked').forEach(cb => {
            preferences.push(cb.value);
        });

        if (preferences.length === 0) {
            showNotification("warn", "Please select at least one travel preference.");
            return;
        }

        // Initialize all days to sunny weather
        const weather_forecast = Array(days).fill("sunny");

        setLoading(true);

        try {
            const response = await fetch("/api/plan", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    destination,
                    preferences,
                    budget_tier,
                    days,
                    pace,
                    weather_forecast
                })
            });

            if (!response.ok) {
                const errDetail = await response.json();
                throw new Error(errDetail.detail || "Failed to generate plan");
            }

            const trip = await response.json();
            currentTrip = trip;
            activeDayIndex = 0;
            
            // Show components
            document.getElementById("stats-panel").style.display = "grid";
            document.getElementById("tabs-panel").style.display = "block";
            document.getElementById("itinerary-content").style.display = "block";
            document.getElementById("chart-panel").style.display = "block";
            document.querySelector(".placeholder-itinerary").style.display = "none";
            
            renderTripUI();
            showNotification("success", `Trip to ${trip.destination} planned successfully!`);
        } catch (err) {
            console.error(err);
            showNotification("error", err.message || "Failed to create trip plan");
        } finally {
            setLoading(false);
        }
    });

    // Simulate Rain Button
    document.getElementById("sim-rain-btn").addEventListener("click", () => {
        simulateWeather("rainy");
    });

    // Simulate Sun Button
    document.getElementById("sim-sun-btn").addEventListener("click", () => {
        simulateWeather("sunny");
    });
}

// Show loading spinner/fade during requests
function setLoading(isLoading) {
    const btn = document.getElementById("generate-btn");
    if (isLoading) {
        btn.disabled = true;
        btn.innerHTML = `<span>Planning...</span> <i class="fa-solid fa-spinner fa-spin"></i>`;
    } else {
        btn.disabled = false;
        btn.innerHTML = `<span>Generate Itinerary</span> <i class="fa-solid fa-wand-magic-sparkles"></i>`;
    }
}

// Render full UI components (Timeline, Tabs, Stats, Maps, Charts)
function renderTripUI() {
    if (!currentTrip) return;
    
    // Update Header Text
    document.getElementById("trip-header-title").textContent = `My Trip to ${currentTrip.destination}, ${currentTrip.country}`;
    document.getElementById("trip-header-desc").textContent = currentTrip.description;

    // Update Stats Row
    document.getElementById("stat-cost").textContent = `$${currentTrip.total_cost.toFixed(2)}`;
    document.getElementById("stat-pace").textContent = currentTrip.pace.charAt(0).toUpperCase() + currentTrip.pace.slice(1);
    document.getElementById("stat-days").textContent = `${currentTrip.days} Day${currentTrip.days > 1 ? 's' : ''}`;

    // Render Day Tabs
    renderDayTabs();

    // Render timeline for active day
    renderActiveDayTimeline();

    // Render Analytics Chart
    renderChart();
}

// Render tabs for each day of the trip
function renderDayTabs() {
    const container = document.getElementById("day-tabs");
    container.innerHTML = "";

    currentTrip.itinerary.forEach((dayData, idx) => {
        const btn = document.createElement("button");
        btn.className = `tab-btn ${idx === activeDayIndex ? 'active' : ''}`;
        
        const weatherIcon = dayData.weather === "rainy" ? "fa-cloud-showers-heavy" : "fa-sun";
        btn.innerHTML = `
            <span>Day ${dayData.day}</span>
            <i class="fa-solid ${weatherIcon}"></i>
        `;
        
        btn.addEventListener("click", () => {
            activeDayIndex = idx;
            // Set active class
            document.querySelectorAll(".tab-btn").forEach(b => b.classList.remove("active"));
            btn.classList.add("active");
            
            renderActiveDayTimeline();
        });
        
        container.appendChild(btn);
    });
}

// Render timeline of activities for selected day
function renderActiveDayTimeline() {
    const dayData = currentTrip.itinerary[activeDayIndex];
    if (!dayData) return;

    // Update Weather header & badge
    document.getElementById("current-day-label").textContent = `Day ${dayData.day}`;
    
    const weatherBadge = document.getElementById("current-day-weather");
    weatherBadge.className = `weather-badge ${dayData.weather}`;
    if (dayData.weather === "rainy") {
        weatherBadge.innerHTML = `<i class="fa-solid fa-cloud-showers-heavy"></i> Rainy`;
    } else {
        weatherBadge.innerHTML = `<i class="fa-solid fa-sun"></i> Sunny`;
    }

    // Render Activities List
    const activitiesList = document.getElementById("activities-list");
    activitiesList.innerHTML = "";

    if (dayData.schedule.length === 0) {
        activitiesList.innerHTML = `
            <div class="text-muted" style="text-align: center; padding: 2rem;">
                No activities scheduled for today. Adjust pace or preferences!
            </div>
        `;
        clearMap();
        return;
    }

    dayData.schedule.forEach((slot, idx) => {
        const act = slot.activity;
        const div = document.createElement("div");
        div.className = "activity-node";
        
        const distText = act.distance_from_prev_km !== undefined 
            ? `<span class="distance-tag"><i class="fa-solid fa-route"></i> +${act.distance_from_prev_km} km from prior spot</span>`
            : `<span class="distance-tag"><i class="fa-solid fa-hotel"></i> Starts near city center</span>`;
            
        div.innerHTML = `
            <div class="node-header">
                <div class="node-title-group">
                    <span class="time-slot-badge">${slot.time_slot}</span>
                    <h4>${act.name}</h4>
                    <div class="activity-meta">
                        <span class="meta-item"><i class="fa-solid fa-star"></i> ${act.rating}</span>
                        <span class="meta-item"><i class="fa-regular fa-clock"></i> ${act.duration_hours}h</span>
                        <span class="cat-badge ${act.category}">${act.category}</span>
                    </div>
                </div>
                <div class="node-cost">${act.cost === 0 ? "Free" : `$${act.cost.toFixed(2)}`}</div>
            </div>
            <p class="node-desc">${act.description}</p>
            <div class="node-footer">
                ${distText}
                <button class="map-link-btn" onclick="focusOnActivity(${act.coords[0]}, ${act.coords[1]}, '${act.name.replace(/'/g, "\\'")}')">
                    <i class="fa-solid fa-location-crosshairs"></i> View on Map
                </button>
            </div>
        `;
        activitiesList.appendChild(div);
    });

    // Update Map
    updateMapForActiveDay();
}

// Center map view on specific activity coordinate
function focusOnActivity(lat, lng, name) {
    if (!map) return;
    map.setView([lat, lng], 15);
    
    // Find and open popup for this activity
    mapMarkers.forEach(marker => {
        const markerLatLng = marker.getLatLng();
        if (markerLatLng.lat === lat && markerLatLng.lng === lng) {
            marker.openPopup();
        }
    });
    
    document.getElementById("map-status-badge").textContent = name;
}

// Make focusOnActivity global so HTML buttons can call it
window.focusOnActivity = focusOnActivity;

// Clear markers and lines on Leaflet
function clearMap() {
    mapMarkers.forEach(m => map.removeLayer(m));
    mapMarkers = [];
    if (routePolyline) {
        map.removeLayer(routePolyline);
        routePolyline = null;
    }
}

// Update Map markers, lines and bounding boxes
function updateMapForActiveDay() {
    clearMap();
    
    const dayData = currentTrip.itinerary[activeDayIndex];
    if (!dayData || dayData.schedule.length === 0) return;

    const latlngs = [];
    
    // Add City Center / Hotel marker as starting point
    const cityCoords = currentTrip.coords;
    latlngs.push(cityCoords);
    
    const centerIcon = L.divIcon({
        className: 'custom-div-icon',
        html: `<div style="background-color: var(--color-teal); width: 14px; height: 14px; border-radius: 50%; border: 2px solid white; box-shadow: 0 0 10px var(--color-teal);"></div>`,
        iconSize: [14, 14],
        iconAnchor: [7, 7]
    });
    
    const centerMarker = L.marker(cityCoords, { icon: centerIcon })
        .addTo(map)
        .bindPopup(`<strong>Basecamp / City Center</strong><br>${currentTrip.destination}`);
    mapMarkers.push(centerMarker);

    // Loop through day activities and place markers
    dayData.schedule.forEach((slot, idx) => {
        const act = slot.activity;
        const coords = act.coords;
        latlngs.push(coords);

        // Marker color code based on category
        let color = "var(--color-indigo)";
        if (act.category === "nature") color = "#22c55e";
        if (act.category === "adventure") color = "#ef4444";
        if (act.category === "food") color = "#f97123";
        if (act.category === "relaxation") color = "#06b6d4";

        const customIcon = L.divIcon({
            className: 'custom-div-icon',
            html: `<div style="background-color: ${color}; width: 22px; height: 22px; border-radius: 50%; border: 3px solid #0f1225; box-shadow: 0 0 10px ${color}; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; font-size: 0.65rem;">${idx + 1}</div>`,
            iconSize: [22, 22],
            iconAnchor: [11, 11]
        });

        const marker = L.marker(coords, { icon: customIcon })
            .addTo(map)
            .bindPopup(`
                <strong>#${idx + 1} ${act.name}</strong><br>
                <small>${slot.time_slot} • ${act.category.toUpperCase()}</small><br>
                Cost: ${act.cost === 0 ? "Free" : "$" + act.cost.toFixed(2)}
            `);
            
        mapMarkers.push(marker);
    });

    // Draw route path line
    routePolyline = L.polyline(latlngs, {
        color: "rgba(99, 102, 241, 0.75)",
        weight: 3,
        dashArray: "6, 6",
        lineCap: "round"
    }).addTo(map);

    // Fit map view to bounds containing all coordinates
    const bounds = L.latLngBounds(latlngs);
    map.fitBounds(bounds, { padding: [40, 40] });
    
    document.getElementById("map-status-badge").textContent = `Day ${dayData.day} Route`;
}

// Generate/Update Budget breakdown analytics chart
function renderChart() {
    if (!currentTrip) return;

    // Collect cost per category across the entire trip
    const categoryCosts = {
        culture: 0,
        nature: 0,
        adventure: 0,
        food: 0,
        relaxation: 0
    };

    currentTrip.itinerary.forEach(day => {
        day.schedule.forEach(slot => {
            const cat = slot.activity.category;
            if (categoryCosts[cat] !== undefined) {
                categoryCosts[cat] += slot.activity.cost;
            }
        });
    });

    // Create colors array matching styling variables
    const colors = {
        culture: "#c084fc",
        nature: "#4ade80",
        adventure: "#f87171",
        food: "#fb923c",
        relaxation: "#22d3ee"
    };

    const labels = Object.keys(categoryCosts).map(key => key.charAt(0).toUpperCase() + key.slice(1));
    const data = Object.values(categoryCosts);
    const backgroundColors = Object.keys(categoryCosts).map(key => colors[key]);

    const ctx = document.getElementById("budget-chart").getContext("2d");

    // Destroy old instance if exists
    if (budgetChart) {
        budgetChart.destroy();
    }

    budgetChart = new Chart(ctx, {
        type: "doughnut",
        data: {
            labels: labels,
            datasets: [{
                data: data,
                backgroundColor: backgroundColors,
                borderWidth: 1,
                borderColor: "rgba(255, 255, 255, 0.15)"
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: "right",
                    labels: {
                        color: "#9ca3af",
                        font: {
                            family: "Inter",
                            size: 11
                        },
                        boxWidth: 12
                    }
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            return ` ${context.label}: $${context.raw.toFixed(2)}`;
                        }
                    }
                }
            },
            cutout: "70%"
        }
    });

    // Update Progress Bar tracking target budget caps
    const totalSpent = currentTrip.total_cost;
    let budgetCap = 350.0; // Mid range default
    
    if (currentTrip.budget_tier === "budget") {
        budgetCap = 100.0;
    } else if (currentTrip.budget_tier === "luxury") {
        budgetCap = 1000.0;
    }

    document.getElementById("budget-limit-text").textContent = `$${totalSpent.toFixed(2)} spent / $${budgetCap} limit`;
    const percentage = Math.min((totalSpent / budgetCap) * 100, 100);
    const progressFill = document.getElementById("budget-progress-bar");
    progressFill.style.width = `${percentage}%`;

    // Visual feedback if over budget
    if (totalSpent > budgetCap) {
        progressFill.style.background = "linear-gradient(to right, var(--color-coral), #ef4444)";
        showNotification("warn", "Budget Alert: Your planned activities exceed the recommended spending cap for this tier!");
    } else {
        progressFill.style.background = "linear-gradient(to right, var(--color-teal), var(--color-indigo))";
    }
}

// Call API to replan a day's activities due to weather change
async function simulateWeather(targetWeather) {
    if (!currentTrip) return;

    const dayData = currentTrip.itinerary[activeDayIndex];
    if (!dayData) return;

    // Check if weather is already the target weather to avoid unnecessary backend calls
    if (dayData.weather === targetWeather) {
        showNotification("info", `Weather is already simulated as ${targetWeather} for Day ${dayData.day}.`);
        return;
    }

    // Build the request body
    const destination = currentTrip.destination;
    
    // Collect checked preferences
    const preferences = [];
    document.querySelectorAll('input[name="preferences"]:checked').forEach(cb => {
        preferences.push(cb.value);
    });

    // Currently scheduled IDs for THIS day (we can re-use or discard them)
    const currently_scheduled_ids = dayData.schedule.map(slot => slot.activity.id);

    // All other used activity IDs across the REST of the trip (exclude these to prevent duplication)
    const all_other_used_ids = [];
    currentTrip.itinerary.forEach((day, idx) => {
        if (idx !== activeDayIndex) {
            day.schedule.forEach(slot => {
                all_other_used_ids.push(slot.activity.id);
            });
        }
    });

    try {
        const response = await fetch("/api/replan-day", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                destination,
                preferences,
                budget_tier: currentTrip.budget_tier,
                pace: currentTrip.pace,
                day_num: dayData.day,
                weather: targetWeather,
                currently_scheduled_ids,
                all_other_used_ids
            })
        });

        if (!response.ok) {
            const errDetail = await response.json();
            throw new Error(errDetail.detail || "Failed to replan day schedule");
        }

        const replannedDayData = await response.json();
        
        // Update local state
        const oldDayCost = dayData.schedule.reduce((sum, slot) => sum + slot.activity.cost, 0);
        const newDayCost = replannedDayData.schedule.reduce((sum, slot) => sum + slot.activity.cost, 0);
        
        currentTrip.itinerary[activeDayIndex] = replannedDayData;
        currentTrip.total_cost = currentTrip.total_cost - oldDayCost + newDayCost;

        // Re-render
        renderTripUI();

        // Push Alert notification on the board
        if (targetWeather === "rainy") {
            const stormMsg = `⚠️ Weather Alert: Rain forecast for Day ${dayData.day} in ${destination}. Outdoor activities replaced with indoor options (e.g. museums, cafes).`;
            showSystemDisruptionAlert(stormMsg);
            showNotification("warn", `Day ${dayData.day} itinerary auto-rerouted to indoor activities!`);
        } else {
            const sunMsg = `☀️ Weather Resolved: Nice skies forecast for Day ${dayData.day} in ${destination}. Schedule restored to standard activities.`;
            showSystemDisruptionAlert(sunMsg);
            showNotification("success", `Day ${dayData.day} itinerary updated for sunny weather!`);
        }

    } catch (err) {
        console.error(err);
        showNotification("error", err.message || "Failed to update schedule for weather changes.");
    }
}

// Render dynamic system warnings/disruptions in the header panel
function showSystemDisruptionAlert(message) {
    const notifyPanel = document.getElementById("notifications");
    
    notifyPanel.innerHTML = `
        <div class="notification-active warn">
            <i class="fa-solid fa-circle-exclamation"></i>
            <div class="notification-body">
                <strong>Real-Time Schedule Shift</strong>
                <span>${message}</span>
            </div>
        </div>
    `;
}

// Toast notification helper (top right of user browser)
function showNotification(type, message) {
    // Create temporary toast container if not exists
    let toastContainer = document.getElementById("toast-container");
    if (!toastContainer) {
        toastContainer = document.createElement("div");
        toastContainer.id = "toast-container";
        toastContainer.style.position = "fixed";
        toastContainer.style.top = "20px";
        toastContainer.style.right = "20px";
        toastContainer.style.zIndex = "9999";
        toastContainer.style.display = "flex";
        toastContainer.style.flexDirection = "column";
        toastContainer.style.gap = "10px";
        document.body.appendChild(toastContainer);
    }

    const toast = document.createElement("div");
    toast.className = "glass";
    toast.style.padding = "1rem 1.25rem";
    toast.style.borderRadius = "12px";
    toast.style.display = "flex";
    toast.style.alignItems = "center";
    toast.style.gap = "0.75rem";
    toast.style.fontSize = "0.85rem";
    toast.style.maxWidth = "320px";
    toast.style.boxShadow = "0 8px 32px 0 rgba(0, 0, 0, 0.4)";
    toast.style.border = "1px solid rgba(255, 255, 255, 0.1)";
    toast.style.animation = "slideIn 0.3s ease-out";
    
    let iconClass = "fa-circle-info";
    let iconColor = "var(--color-indigo)";
    
    if (type === "success") {
        iconClass = "fa-circle-check";
        iconColor = "var(--color-teal)";
        toast.style.background = "rgba(20, 184, 166, 0.15)";
        toast.style.borderColor = "rgba(20, 184, 166, 0.3)";
    } else if (type === "warn") {
        iconClass = "fa-triangle-exclamation";
        iconColor = "var(--color-amber)";
        toast.style.background = "rgba(245, 158, 11, 0.15)";
        toast.style.borderColor = "rgba(245, 158, 11, 0.3)";
    } else if (type === "error") {
        iconClass = "fa-circle-xmark";
        iconColor = "var(--color-coral)";
        toast.style.background = "rgba(244, 63, 94, 0.15)";
        toast.style.borderColor = "rgba(244, 63, 94, 0.3)";
    } else {
        toast.style.background = "rgba(13, 17, 39, 0.85)";
    }

    toast.innerHTML = `
        <i class="fa-solid ${iconClass}" style="color: ${iconColor}; font-size: 1.1rem;"></i>
        <span style="color: white; font-weight: 500;">${message}</span>
    `;

    toastContainer.appendChild(toast);

    // Auto remove toast
    setTimeout(() => {
        toast.style.animation = "fadeIn 0.3s ease-out reverse";
        setTimeout(() => {
            toast.remove();
        }, 300);
    }, 4000);
}
