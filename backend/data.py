# backend/data.py

from typing import Dict, List, Any

DESTINATIONS: Dict[str, Dict[str, Any]] = {
    "Tokyo": {
        "name": "Tokyo",
        "country": "Japan",
        "description": "A high-tech metropolis blended with ancient temples, bustling markets, and world-class cuisine.",
        "coords": [35.6762, 139.6503],
        "activities": [
            {
                "id": "tky_sensoji",
                "name": "Sensō-ji Temple",
                "description": "Tokyo's oldest and most iconic Buddhist temple in Asakusa.",
                "category": "culture",
                "cost": 0.0,
                "duration_hours": 1.5,
                "coords": [35.7148, 139.7967],
                "is_outdoor": True,
                "rating": 4.8
            },
            {
                "id": "tky_skytree",
                "name": "Tokyo Skytree",
                "description": "Soar above the city at one of the tallest structures in the world.",
                "category": "adventure",
                "cost": 25.0,
                "duration_hours": 2.0,
                "coords": [35.7101, 139.8107],
                "is_outdoor": False,
                "rating": 4.7
            },
            {
                "id": "tky_shinjuku_gyoen",
                "name": "Shinjuku Gyoen National Garden",
                "description": "A peaceful escape featuring traditional Japanese, English, and French gardens.",
                "category": "nature",
                "cost": 5.0,
                "duration_hours": 2.0,
                "coords": [35.6852, 139.7101],
                "is_outdoor": True,
                "rating": 4.6
            },
            {
                "id": "tky_teamlab",
                "name": "teamLab Planets",
                "description": "An immersive digital art museum where you walk through water and gardens.",
                "category": "culture",
                "cost": 32.0,
                "duration_hours": 2.5,
                "coords": [35.6491, 139.7909],
                "is_outdoor": False,
                "rating": 4.9
            },
            {
                "id": "tky_tsukiji",
                "name": "Tsukiji Outer Market Food Tour",
                "description": "Taste fresh sushi and traditional street food in this lively market.",
                "category": "food",
                "cost": 20.0,
                "duration_hours": 1.5,
                "coords": [35.6654, 139.7700],
                "is_outdoor": True,
                "rating": 4.7
            },
            {
                "id": "tky_meiji",
                "name": "Meiji Jingu Shrine",
                "description": "Shinto shrine surrounded by a dense forest in the heart of Shibuya.",
                "category": "culture",
                "cost": 0.0,
                "duration_hours": 1.5,
                "coords": [35.6764, 139.6993],
                "is_outdoor": True,
                "rating": 4.7
            },
            {
                "id": "tky_akihabara",
                "name": "Akihabara Electric Town Tour",
                "description": "Explore electronics stores, retro game centers, and anime culture shops.",
                "category": "adventure",
                "cost": 10.0,
                "duration_hours": 2.0,
                "coords": [35.6997, 139.7715],
                "is_outdoor": False,
                "rating": 4.5
            },
            {
                "id": "tky_samurai",
                "name": "Samurai Museum & Katana Demonstration",
                "description": "Learn about the samurai code and experience a sword demonstration.",
                "category": "culture",
                "cost": 18.0,
                "duration_hours": 1.5,
                "coords": [35.6953, 139.7022],
                "is_outdoor": False,
                "rating": 4.6
            },
            {
                "id": "tky_shibuya",
                "name": "Shibuya Crossing & Rooftop Cafe",
                "description": "Watch the famous pedestrian scramble from a cozy rooftop spot.",
                "category": "relaxation",
                "cost": 8.0,
                "duration_hours": 1.0,
                "coords": [35.6595, 139.7005],
                "is_outdoor": False,
                "rating": 4.8
            },
            {
                "id": "tky_ghibli",
                "name": "Ghibli Museum",
                "description": "The magical museum of legendary animation house Studio Ghibli.",
                "category": "culture",
                "cost": 10.0,
                "duration_hours": 3.0,
                "coords": [35.6963, 139.5704],
                "is_outdoor": False,
                "rating": 4.9
            }
        ]
    },
    "Reykjavik": {
        "name": "Reykjavik",
        "country": "Iceland",
        "description": "Gateway to dramatic landscapes, hot springs, towering waterfalls, and northern lights.",
        "coords": [64.1466, -21.9426],
        "activities": [
            {
                "id": "rey_blue_lagoon",
                "name": "Blue Lagoon Geothermal Spa",
                "description": "Relax in mineral-rich, milky-blue geothermal waters surrounded by lava fields.",
                "category": "relaxation",
                "cost": 85.0,
                "duration_hours": 3.0,
                "coords": [63.8794, -22.4498],
                "is_outdoor": True,
                "rating": 4.8
            },
            {
                "id": "rey_hallgrimskirkja",
                "name": "Hallgrímskirkja Church & Tower",
                "description": "A stunning expressionist cathedral inspired by basalt lava flows.",
                "category": "culture",
                "cost": 10.0,
                "duration_hours": 1.0,
                "coords": [64.1418, -21.9266],
                "is_outdoor": False,
                "rating": 4.6
            },
            {
                "id": "rey_geysir",
                "name": "Golden Circle Geysir Explorer",
                "description": "Witness the powerful Strokkur geysir erupting boiling water high into the sky.",
                "category": "nature",
                "cost": 50.0,
                "duration_hours": 4.0,
                "coords": [64.3129, -20.3012],
                "is_outdoor": True,
                "rating": 4.7
            },
            {
                "id": "rey_gullfoss",
                "name": "Gullfoss Waterfall Hike",
                "description": "A spectacular double waterfall where the river Hvíta plunges into a crevice.",
                "category": "nature",
                "cost": 0.0,
                "duration_hours": 1.5,
                "coords": [64.3271, -20.1199],
                "is_outdoor": True,
                "rating": 4.9
            },
            {
                "id": "rey_perlan",
                "name": "Perlan Wonders of Iceland Museum",
                "description": "Features a real indoor ice cave, planetarium northern lights show, and observation deck.",
                "category": "culture",
                "cost": 30.0,
                "duration_hours": 2.5,
                "coords": [64.1292, -21.9189],
                "is_outdoor": False,
                "rating": 4.5
            },
            {
                "id": "rey_harpa",
                "name": "Harpa Concert Hall Tour",
                "description": "Stunning modern architecture with a colored glass facade inspired by basalt rocks.",
                "category": "culture",
                "cost": 0.0,
                "duration_hours": 1.0,
                "coords": [64.1504, -21.9326],
                "is_outdoor": False,
                "rating": 4.6
            },
            {
                "id": "rey_whales",
                "name": "Whale Watching Rib Boat Tour",
                "description": "Go searching for humpback whales, minke whales, and dolphins off the coast.",
                "category": "adventure",
                "cost": 75.0,
                "duration_hours": 3.0,
                "coords": [64.1542, -21.9472],
                "is_outdoor": True,
                "rating": 4.7
            },
            {
                "id": "rey_aurora_center",
                "name": "Aurora Reykjavik Center",
                "description": "An interactive exhibition on the science and folklore of the Northern Lights.",
                "category": "culture",
                "cost": 18.0,
                "duration_hours": 1.5,
                "coords": [64.1528, -21.9485],
                "is_outdoor": False,
                "rating": 4.6
            },
            {
                "id": "rey_thingvellir",
                "name": "Þingvellir National Park Hike",
                "description": "Walk between the North American and Eurasian tectonic plates at this historic site.",
                "category": "nature",
                "cost": 0.0,
                "duration_hours": 3.0,
                "coords": [64.2559, -21.1297],
                "is_outdoor": True,
                "rating": 4.8
            },
            {
                "id": "rey_pool",
                "name": "Laugardalslaug Thermal Pool",
                "description": "Reykjavik's largest public geothermal pool with hot tubs and steam baths.",
                "category": "relaxation",
                "cost": 9.0,
                "duration_hours": 2.0,
                "coords": [64.1462, -21.8791],
                "is_outdoor": True,
                "rating": 4.6
            }
        ]
    },
    "Paris": {
        "name": "Paris",
        "country": "France",
        "description": "The global center of art, fashion, gastronomy, and historic architecture along the Seine.",
        "coords": [48.8566, 2.3522],
        "activities": [
            {
                "id": "par_eiffel",
                "name": "Eiffel Tower Ascent",
                "description": "Climb up to the summit for breathtaking vistas of Paris.",
                "category": "culture",
                "cost": 28.0,
                "duration_hours": 2.0,
                "coords": [48.8584, 2.2945],
                "is_outdoor": True,
                "rating": 4.8
            },
            {
                "id": "par_louvre",
                "name": "Louvre Museum Tour",
                "description": "Explore masterpieces like the Mona Lisa and Venus de Milo in a historic palace.",
                "category": "culture",
                "cost": 22.0,
                "duration_hours": 3.5,
                "coords": [48.8606, 2.3376],
                "is_outdoor": False,
                "rating": 4.9
            },
            {
                "id": "par_versailles",
                "name": "Palace of Versailles Daytrip",
                "description": "Tour the breathtaking Hall of Mirrors and vast manicured gardens.",
                "category": "culture",
                "cost": 25.0,
                "duration_hours": 4.0,
                "coords": [48.8049, 2.1204],
                "is_outdoor": False,
                "rating": 4.8
            },
            {
                "id": "par_seine",
                "name": "Seine River Sunset Cruise",
                "description": "A relaxing cruise down the Seine, viewing monuments lit up at night.",
                "category": "relaxation",
                "cost": 18.0,
                "duration_hours": 1.5,
                "coords": [48.8623, 2.3278],
                "is_outdoor": True,
                "rating": 4.6
            },
            {
                "id": "par_orsay",
                "name": "Musée d'Orsay",
                "description": "World-famous collection of Impressionist and Post-Impressionist art in a grand railway station.",
                "category": "culture",
                "cost": 16.0,
                "duration_hours": 2.5,
                "coords": [48.8600, 2.3266],
                "is_outdoor": False,
                "rating": 4.8
            },
            {
                "id": "par_montmartre",
                "name": "Sacré-Cœur & Montmartre Art Walk",
                "description": "Wander the cobbled streets of the artist district and visit the basilica.",
                "category": "culture",
                "cost": 0.0,
                "duration_hours": 2.0,
                "coords": [48.8867, 2.3431],
                "is_outdoor": True,
                "rating": 4.7
            },
            {
                "id": "par_food_tour",
                "name": "Latin Quarter Pastry & Cheese Tour",
                "description": "Indulge in artisanal cheeses, croissants, macarons, and French wines.",
                "category": "food",
                "cost": 65.0,
                "duration_hours": 3.0,
                "coords": [48.8482, 2.3458],
                "is_outdoor": True,
                "rating": 4.8
            },
            {
                "id": "par_catacombs",
                "name": "Catacombs of Paris",
                "description": "Descend into the underground ossuaries containing the remains of millions.",
                "category": "adventure",
                "cost": 29.0,
                "duration_hours": 2.0,
                "coords": [48.8338, 2.3324],
                "is_outdoor": False,
                "rating": 4.5
            },
            {
                "id": "par_luxembourg",
                "name": "Jardin du Luxembourg",
                "description": "Stroll past statues, fountains, and beautiful flowerbeds in this tranquil park.",
                "category": "nature",
                "cost": 0.0,
                "duration_hours": 1.5,
                "coords": [48.8462, 2.3372],
                "is_outdoor": True,
                "rating": 4.7
            },
            {
                "id": "par_notredame",
                "name": "Notre-Dame Cathedral & Latin Quarter Walk",
                "description": "Admire the Gothic facade of Notre-Dame and walk along historical bookstands.",
                "category": "culture",
                "cost": 0.0,
                "duration_hours": 1.0,
                "coords": [48.8530, 2.3499],
                "is_outdoor": True,
                "rating": 4.6
            }
        ]
    },
    "New York": {
        "name": "New York",
        "country": "United States",
        "description": "The city that never sleeps, known for theater, high-rise architecture, diverse foods, and leafy parks.",
        "coords": [40.7128, -74.0060],
        "activities": [
            {
                "id": "nyc_central_park",
                "name": "Central Park Walking Tour",
                "description": "Discover Bethesda Fountain, Strawberry Fields, and sheep meadow in NYC's heart.",
                "category": "nature",
                "cost": 0.0,
                "duration_hours": 2.5,
                "coords": [40.7851, -73.9683],
                "is_outdoor": True,
                "rating": 4.8
            },
            {
                "id": "nyc_empire",
                "name": "Empire State Building Observatory",
                "description": "Classic views of Manhattan from the iconic 86th-floor open-air deck.",
                "category": "culture",
                "cost": 44.0,
                "duration_hours": 2.0,
                "coords": [40.7484, -73.9857],
                "is_outdoor": False,
                "rating": 4.6
            },
            {
                "id": "nyc_met",
                "name": "Metropolitan Museum of Art",
                "description": "One of the world's greatest art museums, spanning over 5,000 years of history.",
                "category": "culture",
                "cost": 30.0,
                "duration_hours": 3.0,
                "coords": [40.7794, -73.9632],
                "is_outdoor": False,
                "rating": 4.8
            },
            {
                "id": "nyc_statue",
                "name": "Statue of Liberty & Ellis Island",
                "description": "Take the ferry to visit Liberty Island and explore the historic immigration museum.",
                "category": "culture",
                "cost": 24.0,
                "duration_hours": 3.5,
                "coords": [40.6892, -74.0445],
                "is_outdoor": True,
                "rating": 4.7
            },
            {
                "id": "nyc_broadway",
                "name": "Broadway Show Experience",
                "description": "Attend a world-class theater production in the famous Theatre District.",
                "category": "culture",
                "cost": 110.0,
                "duration_hours": 3.0,
                "coords": [40.7590, -73.9845],
                "is_outdoor": False,
                "rating": 4.9
            },
            {
                "id": "nyc_highline",
                "name": "High Line Park Stroll",
                "description": "A public park built on a historic freight rail line elevated above Chelsea.",
                "category": "nature",
                "cost": 0.0,
                "duration_hours": 1.5,
                "coords": [40.7480, -74.0048],
                "is_outdoor": True,
                "rating": 4.7
            },
            {
                "id": "nyc_chelsea",
                "name": "Chelsea Market Food Crawl",
                "description": "Sample lobster rolls, tacos, and artisan chocolates inside a historic biscuit factory.",
                "category": "food",
                "cost": 40.0,
                "duration_hours": 2.0,
                "coords": [40.7420, -74.0062],
                "is_outdoor": False,
                "rating": 4.7
            },
            {
                "id": "nyc_edge",
                "name": "Edge Observation Deck",
                "description": "Stand on the highest outdoor sky deck in the Western Hemisphere with glass floors.",
                "category": "adventure",
                "cost": 40.0,
                "duration_hours": 1.5,
                "coords": [40.7538, -74.0010],
                "is_outdoor": True,
                "rating": 4.7
            },
            {
                "id": "nyc_moma",
                "name": "Museum of Modern Art (MoMA)",
                "description": "Home to Van Gogh's Starry Night, Warhol's Soup Cans, and contemporary masterpieces.",
                "category": "culture",
                "cost": 25.0,
                "duration_hours": 2.0,
                "coords": [40.7614, -73.9776],
                "is_outdoor": False,
                "rating": 4.7
            },
            {
                "id": "nyc_brooklyn_bridge",
                "name": "Brooklyn Bridge Walk",
                "description": "Walk across the historic suspension bridge and enjoy views of the city skyline.",
                "category": "adventure",
                "cost": 0.0,
                "duration_hours": 1.5,
                "coords": [40.7061, -73.9969],
                "is_outdoor": True,
                "rating": 4.8
            }
        ]
    },
    "Rome": {
        "name": "Rome",
        "country": "Italy",
        "description": "A historic treasure chest filled with Roman ruins, Baroque fountains, and mouthwatering pasta.",
        "coords": [41.9028, 12.4964],
        "activities": [
            {
                "id": "rom_colosseum",
                "name": "Colosseum & Roman Forum",
                "description": "Walk inside the world's largest ancient amphitheater and the heart of the Roman Empire.",
                "category": "culture",
                "cost": 18.0,
                "duration_hours": 3.0,
                "coords": [41.8902, 12.4922],
                "is_outdoor": True,
                "rating": 4.9
            },
            {
                "id": "rom_vatican",
                "name": "Vatican Museums & Sistine Chapel",
                "description": "Marvel at Michelangelo's ceiling frescoes and centuries of papal art collections.",
                "category": "culture",
                "cost": 25.0,
                "duration_hours": 3.5,
                "coords": [41.9067, 12.4526],
                "is_outdoor": False,
                "rating": 4.9
            },
            {
                "id": "rom_trevi",
                "name": "Trevi Fountain Coin Toss",
                "description": "Toss a coin into Rome's most famous Baroque masterpiece to ensure your return.",
                "category": "relaxation",
                "cost": 0.0,
                "duration_hours": 1.0,
                "coords": [41.9009, 12.4833],
                "is_outdoor": True,
                "rating": 4.8
            },
            {
                "id": "rom_pantheon",
                "name": "The Pantheon",
                "description": "Admire the ancient temple's concrete dome and open oculus, standing for 2,000 years.",
                "category": "culture",
                "cost": 5.0,
                "duration_hours": 1.0,
                "coords": [41.8986, 12.4769],
                "is_outdoor": False,
                "rating": 4.7
            },
            {
                "id": "rom_borghese",
                "name": "Borghese Gallery & Villa Gardens",
                "description": "See Bernini sculptures and Raphael paintings, then walk through lush villa gardens.",
                "category": "nature",
                "cost": 15.0,
                "duration_hours": 2.5,
                "coords": [41.9142, 12.4921],
                "is_outdoor": False,
                "rating": 4.8
            },
            {
                "id": "rom_trastevere",
                "name": "Trastevere Food & Wine Crawl",
                "description": "Wander charming lanes to try supplì, Roman pizza, cacio e pepe, and local wines.",
                "category": "food",
                "cost": 55.0,
                "duration_hours": 3.0,
                "coords": [41.8885, 12.4707],
                "is_outdoor": True,
                "rating": 4.8
            },
            {
                "id": "rom_castel",
                "name": "Castel Sant'Angelo Castle Tour",
                "description": "Explore the historic fortress that served as a mausoleum, fortress, and papal refuge.",
                "category": "culture",
                "cost": 12.0,
                "duration_hours": 1.5,
                "coords": [41.9031, 12.4663],
                "is_outdoor": False,
                "rating": 4.6
            },
            {
                "id": "rom_spanish_steps",
                "name": "Spanish Steps & Gelato Walk",
                "description": "Stroll down the famous monumental stairway and browse surrounding designer streets.",
                "category": "relaxation",
                "cost": 7.0,
                "duration_hours": 1.0,
                "coords": [41.9060, 12.4828],
                "is_outdoor": True,
                "rating": 4.5
            },
            {
                "id": "rom_catacombs",
                "name": "Catacombs of St. Callixtus",
                "description": "Descend into the underground galleries where early Christians were buried.",
                "category": "adventure",
                "cost": 10.0,
                "duration_hours": 2.0,
                "coords": [41.8605, 12.5103],
                "is_outdoor": False,
                "rating": 4.5
            },
            {
                "id": "rom_piazza_navona",
                "name": "Piazza Navona Street Artist Tour",
                "description": "See the Fountain of the Four Rivers and enjoy street performers in this lively square.",
                "category": "culture",
                "cost": 0.0,
                "duration_hours": 1.0,
                "coords": [41.8988, 12.4731],
                "is_outdoor": True,
                "rating": 4.7
            }
        ]
    },
    "Delhi": {
        "name": "Delhi",
        "country": "India",
        "description": "India's capital, a massive metropolitan area blending ancient monuments, historic markets, and lush government complexes.",
        "coords": [28.6139, 77.2090],
        "activities": [
            {
                "id": "del_red_fort",
                "name": "Red Fort Heritage Tour",
                "description": "Explore the historic red sandstone fortress built by Emperor Shah Jahan.",
                "category": "culture",
                "cost": 8.0,
                "duration_hours": 2.5,
                "coords": [28.6562, 77.2410],
                "is_outdoor": True,
                "rating": 4.6
            },
            {
                "id": "del_qutub_minar",
                "name": "Qutub Minar Complex",
                "description": "Admire the towering 73-meter minaret and ancient iron pillar.",
                "category": "culture",
                "cost": 8.0,
                "duration_hours": 2.0,
                "coords": [28.5244, 77.1855],
                "is_outdoor": True,
                "rating": 4.7
            },
            {
                "id": "del_akshardham",
                "name": "Swaminarayan Akshardham Temple Exhibition",
                "description": "Marvel at the giant stone architecture and indoor boat ride exhibition.",
                "category": "culture",
                "cost": 3.0,
                "duration_hours": 3.5,
                "coords": [28.6127, 77.2773],
                "is_outdoor": False,
                "rating": 4.9
            },
            {
                "id": "del_chandni_chowk",
                "name": "Chandni Chowk Street Food Crawl",
                "description": "Taste historic paranthas, jalebis, and chaat in Old Delhi's narrow lanes.",
                "category": "food",
                "cost": 15.0,
                "duration_hours": 2.5,
                "coords": [28.6560, 77.2300],
                "is_outdoor": True,
                "rating": 4.8
            },
            {
                "id": "del_national_museum",
                "name": "National Museum of India",
                "description": "Browse prehistoric relics, bronze sculptures, and royal relics.",
                "category": "culture",
                "cost": 6.0,
                "duration_hours": 3.0,
                "coords": [28.6118, 77.2193],
                "is_outdoor": False,
                "rating": 4.5
            },
            {
                "id": "del_lodhi_gardens",
                "name": "Lodhi Gardens Picnic & Walk",
                "description": "A tranquil green oasis containing tombs of 15th-century rulers.",
                "category": "nature",
                "cost": 0.0,
                "duration_hours": 2.0,
                "coords": [28.5933, 77.2189],
                "is_outdoor": True,
                "rating": 4.7
            },
            {
                "id": "del_humayun_tomb",
                "name": "Humayun's Tomb Garden Walk",
                "description": "Stunning precursor to the Taj Mahal, set inside symmetric Persian gardens.",
                "category": "culture",
                "cost": 8.0,
                "duration_hours": 2.0,
                "coords": [28.5847, 77.2509],
                "is_outdoor": True,
                "rating": 4.8
            },
            {
                "id": "del_india_gate",
                "name": "India Gate & Kartavya Path Walk",
                "description": "Walk down the grand boulevard to the national war memorial.",
                "category": "relaxation",
                "cost": 0.0,
                "duration_hours": 1.0,
                "coords": [28.6129, 77.2295],
                "is_outdoor": True,
                "rating": 4.6
            },
            {
                "id": "del_dilli_haat",
                "name": "Dilli Haat Craft Market Bazaar",
                "description": "Shop for traditional tribal crafts and sample food from various states.",
                "category": "food",
                "cost": 1.0,
                "duration_hours": 2.0,
                "coords": [28.5732, 77.2081],
                "is_outdoor": True,
                "rating": 4.5
            },
            {
                "id": "del_rashtrapati",
                "name": "Rashtrapati Bhavan Gallery Tour",
                "description": "See the grand presidential halls and historical museums.",
                "category": "culture",
                "cost": 1.0,
                "duration_hours": 2.0,
                "coords": [28.6143, 77.2005],
                "is_outdoor": False,
                "rating": 4.6
            }
        ]
    },
    "Goa": {
        "name": "Goa",
        "country": "India",
        "description": "Coastal paradise famous for beaches, Portuguese architecture, ancient spice farms, and seafood.",
        "coords": [15.4909, 73.8278],
        "activities": [
            {
                "id": "goa_water_sports",
                "name": "Calangute Beach Para-Sailing & Jet Skiing",
                "description": "Experience thrilling water sports on Goa's most active beach strip.",
                "category": "adventure",
                "cost": 22.0,
                "duration_hours": 2.0,
                "coords": [15.5494, 73.7535],
                "is_outdoor": True,
                "rating": 4.7
            },
            {
                "id": "goa_dudhsagar",
                "name": "Dudhsagar Waterfalls Trek & Jeep Safari",
                "description": "A magnificent four-tiered waterfall surrounded by dense tropical forest.",
                "category": "nature",
                "cost": 12.0,
                "duration_hours": 4.5,
                "coords": [15.3134, 74.3142],
                "is_outdoor": True,
                "rating": 4.8
            },
            {
                "id": "goa_bom_jesus",
                "name": "Basilica of Bom Jesus Tour",
                "description": "UNESCO site holding the mortal remains of St. Francis Xavier.",
                "category": "culture",
                "cost": 0.0,
                "duration_hours": 1.5,
                "coords": [15.5009, 73.9116],
                "is_outdoor": False,
                "rating": 4.7
            },
            {
                "id": "goa_fontainhas",
                "name": "Fontainhas Latin Quarter Walking Tour",
                "description": "Wander past colorful Portuguese colonial houses with tiled roofs.",
                "category": "culture",
                "cost": 0.0,
                "duration_hours": 1.5,
                "coords": [15.4989, 73.8440],
                "is_outdoor": True,
                "rating": 4.6
            },
            {
                "id": "goa_cruise",
                "name": "Mandovi River Dinner Cruise",
                "description": "Sunset cruise with traditional Goan folk dances, music, and buffet dining.",
                "category": "food",
                "cost": 25.0,
                "duration_hours": 2.5,
                "coords": [15.4986, 73.8278],
                "is_outdoor": True,
                "rating": 4.5
            },
            {
                "id": "goa_spice_farm",
                "name": "Sahakari Spice Plantation Tour & Lunch",
                "description": "Guided walk showing organic spices followed by a traditional Goan buffet.",
                "category": "food",
                "cost": 10.0,
                "duration_hours": 3.0,
                "coords": [15.4056, 74.0200],
                "is_outdoor": True,
                "rating": 4.7
            },
            {
                "id": "goa_anjuna_market",
                "name": "Anjuna Flea Market & Sunset Stroll",
                "description": "Browse bohemian crafts and enjoy beachside views.",
                "category": "relaxation",
                "cost": 0.0,
                "duration_hours": 2.0,
                "coords": [15.5804, 73.7445],
                "is_outdoor": True,
                "rating": 4.5
            },
            {
                "id": "goa_curlies",
                "name": "Curlies Shack Beach Dining",
                "description": "Relax on sunbeds with seafood and drinks at Anjuna beach.",
                "category": "food",
                "cost": 15.0,
                "duration_hours": 2.0,
                "coords": [15.5724, 73.7431],
                "is_outdoor": True,
                "rating": 4.6
            },
            {
                "id": "goa_chapora_fort",
                "name": "Chapora Fort Sunset Hike",
                "description": "Famous clifftop ruins offering panoramic views of Vagator beach.",
                "category": "adventure",
                "cost": 0.0,
                "duration_hours": 1.5,
                "coords": [15.6062, 73.7354],
                "is_outdoor": True,
                "rating": 4.7
            },
            {
                "id": "goa_science_center",
                "name": "Goa Science Centre & Planetarium",
                "description": "Modern science exhibition halls and astronomical planetarium.",
                "category": "culture",
                "cost": 2.0,
                "duration_hours": 2.0,
                "coords": [15.4800, 73.8090],
                "is_outdoor": False,
                "rating": 4.4
            }
        ]
    },
    "Mumbai": {
        "name": "Mumbai",
        "country": "India",
        "description": "India's financial capital, home to Bollywood, grand colonial buildings, and coastal promenades.",
        "coords": [18.9220, 72.8347],
        "activities": [
            {
                "id": "mum_gateway",
                "name": "Gateway of India & Taj Mahal Palace Walk",
                "description": "Stand before the monumental arch and view the historic Taj Mahal Palace hotel.",
                "category": "culture",
                "cost": 0.0,
                "duration_hours": 1.5,
                "coords": [18.9220, 72.8347],
                "is_outdoor": True,
                "rating": 4.8
            },
            {
                "id": "mum_marine_drive",
                "name": "Marine Drive Promenade Sunset Stroll",
                "description": "Walk along the curved bay known as the 'Queen's Necklace' for a sea breeze.",
                "category": "relaxation",
                "cost": 0.0,
                "duration_hours": 1.5,
                "coords": [18.9415, 72.8236],
                "is_outdoor": True,
                "rating": 4.7
            },
            {
                "id": "mum_museum",
                "name": "Chhatrapati Shivaji Maharaj Vastu Sangrahalaya",
                "description": "Explore the primary art and history museum in Mumbai's indo-saracenic dome building.",
                "category": "culture",
                "cost": 10.0,
                "duration_hours": 3.0,
                "coords": [18.9269, 72.8327],
                "is_outdoor": False,
                "rating": 4.8
            },
            {
                "id": "mum_crawford",
                "name": "Crawford Market & Shopping Bazaar",
                "description": "Explore the historic Victorian market for spices, fruits, and wholesale products.",
                "category": "culture",
                "cost": 5.0,
                "duration_hours": 2.0,
                "coords": [18.9472, 72.8333],
                "is_outdoor": False,
                "rating": 4.4
            },
            {
                "id": "mum_national_park",
                "name": "Kanheri Caves Hike & Sanjay Gandhi Park",
                "description": "Explore ancient rock-cut Buddhist caves nestled deep inside a national park.",
                "category": "nature",
                "cost": 10.0,
                "duration_hours": 4.0,
                "coords": [19.2291, 72.9184],
                "is_outdoor": True,
                "rating": 4.7
            },
            {
                "id": "mum_colaba",
                "name": "Colaba Causeway Cafe & Street Crawl",
                "description": "Try Leopold Cafe and shop for antiquities and jewelry along the busy street.",
                "category": "food",
                "cost": 12.0,
                "duration_hours": 2.0,
                "coords": [18.9180, 72.8280],
                "is_outdoor": True,
                "rating": 4.6
            },
            {
                "id": "mum_elephanta",
                "name": "Elephanta Caves Cruise & Rock Temple Tour",
                "description": "Take a ferry to Elephanta island and view cave temples dedicated to Shiva.",
                "category": "adventure",
                "cost": 8.0,
                "duration_hours": 4.0,
                "coords": [18.9633, 72.9315],
                "is_outdoor": True,
                "rating": 4.5
            },
            {
                "id": "mum_juhu",
                "name": "Juhu Beach Chowpatty Snacks Tour",
                "description": "Indulge in Pav Bhaji, Bhel Puri, and Gola by the Arabian sea shoreline.",
                "category": "food",
                "cost": 6.0,
                "duration_hours": 1.5,
                "coords": [19.0988, 72.8264],
                "is_outdoor": True,
                "rating": 4.6
            },
            {
                "id": "mum_science",
                "name": "Nehru Science Center & Space Planetarium",
                "description": "Interactive physics exhibits and giant 3D dome planetarium.",
                "category": "culture",
                "cost": 3.0,
                "duration_hours": 2.5,
                "coords": [18.9899, 72.8184],
                "is_outdoor": False,
                "rating": 4.5
            },
            {
                "id": "mum_mani",
                "name": "Mani Bhavan Gandhi Museum",
                "description": "Learn about Gandhi's movements inside his residence during the struggle.",
                "category": "culture",
                "cost": 0.50,
                "duration_hours": 1.5,
                "coords": [18.9602, 72.8123],
                "is_outdoor": False,
                "rating": 4.7
            }
        ]
    },
    "Bengaluru": {
        "name": "Bengaluru",
        "country": "India",
        "description": "India's high-tech hub, renowned for its pleasant climate, parks, food streets, and craft breweries.",
        "coords": [12.9716, 77.5946],
        "activities": [
            {
                "id": "blr_lalbagh",
                "name": "Lalbagh Botanical Garden walk",
                "description": "Stroll past a historic glasshouse and centuries-old trees.",
                "category": "nature",
                "cost": 1.0,
                "duration_hours": 2.0,
                "coords": [12.9507, 77.5900],
                "is_outdoor": True,
                "rating": 4.6
            },
            {
                "id": "blr_palace",
                "name": "Bangalore Palace Royal Tour",
                "description": "See Tudor-style architecture and woodcarvings inside the royal family's urban castle.",
                "category": "culture",
                "cost": 6.0,
                "duration_hours": 2.0,
                "coords": [12.9987, 77.5921],
                "is_outdoor": False,
                "rating": 4.6
            },
            {
                "id": "blr_cubbon",
                "name": "Cubbon Park Jog & Bamboo Grove Walk",
                "description": "Lush central park with libraries, museum structures, and massive bamboo fields.",
                "category": "nature",
                "cost": 0.0,
                "duration_hours": 1.5,
                "coords": [12.9739, 77.5960],
                "is_outdoor": True,
                "rating": 4.7
            },
            {
                "id": "blr_food_street",
                "name": "VV Puram Thindi Beedi Food Crawl",
                "description": "Feast on capsicum bhaji, akki roti, honey jalebis, and multi-flavored idlis.",
                "category": "food",
                "cost": 8.0,
                "duration_hours": 2.0,
                "coords": [12.9525, 77.5772],
                "is_outdoor": True,
                "rating": 4.8
            },
            {
                "id": "blr_museum",
                "name": "Visvesvaraya Technological Museum",
                "description": "Interact with space modules, engine gear configurations, and dinosaurs.",
                "category": "culture",
                "cost": 2.0,
                "duration_hours": 3.0,
                "coords": [12.9752, 77.6006],
                "is_outdoor": False,
                "rating": 4.5
            },
            {
                "id": "blr_nandi",
                "name": "Nandi Hills Sunrise & Hiking Trek",
                "description": "Ascend the fort mountain before sunrise to view clouds beneath the summit.",
                "category": "adventure",
                "cost": 3.0,
                "duration_hours": 4.0,
                "coords": [13.3702, 77.6835],
                "is_outdoor": True,
                "rating": 4.7
            },
            {
                "id": "blr_ngma",
                "name": "National Gallery of Modern Art Bangalore",
                "description": "Modern painting collections housed inside a grand heritage mansion.",
                "category": "culture",
                "cost": 4.0,
                "duration_hours": 2.0,
                "coords": [12.9918, 77.5888],
                "is_outdoor": False,
                "rating": 4.6
            },
            {
                "id": "blr_safari",
                "name": "Bannerghatta Safari & Butterfly Park",
                "description": "Observe Bengal tigers, Asiatic lions, and bears from caged bus safaris.",
                "category": "nature",
                "cost": 15.0,
                "duration_hours": 4.0,
                "coords": [12.7936, 77.5746],
                "is_outdoor": True,
                "rating": 4.5
            },
            {
                "id": "blr_brewery",
                "name": "Indiranagar Microbrewery Hopping",
                "description": "Sample fresh local craft beers and premium gastro-pub bites.",
                "category": "food",
                "cost": 25.0,
                "duration_hours": 3.0,
                "coords": [12.9718, 77.6411],
                "is_outdoor": False,
                "rating": 4.7
            },
            {
                "id": "blr_wonderla",
                "name": "Wonderla Amusement Park Outing",
                "description": "High thrill rollercoasters and giant wave pool parks.",
                "category": "adventure",
                "cost": 20.0,
                "duration_hours": 5.0,
                "coords": [12.7397, 77.3995],
                "is_outdoor": True,
                "rating": 4.6
            }
        ]
    },
    "Jaipur": {
        "name": "Jaipur",
        "country": "India",
        "description": "The capital of Rajasthan, famously called the 'Pink City' due to its terracotta palace walls and forts.",
        "coords": [26.9124, 75.7873],
        "activities": [
            {
                "id": "jai_amber",
                "name": "Amber Palace & Maota Lake Overlook",
                "description": "Tour the grand hilltop fort using cobblestone pathways, viewing sheer luxury courtyards.",
                "category": "culture",
                "cost": 10.0,
                "duration_hours": 3.0,
                "coords": [26.9855, 75.8513],
                "is_outdoor": True,
                "rating": 4.9
            },
            {
                "id": "jai_hawa_mahal",
                "name": "Hawa Mahal (Palace of Winds)",
                "description": "Marvel at the pink honeycomb screen structure built so royal women could watch streets.",
                "category": "culture",
                "cost": 3.0,
                "duration_hours": 1.5,
                "coords": [26.9239, 75.8267],
                "is_outdoor": True,
                "rating": 4.7
            },
            {
                "id": "jai_city_palace",
                "name": "City Palace Museum Tour",
                "description": "Explore royal courtyards, armories, and Peacock Gate entrypoints.",
                "category": "culture",
                "cost": 8.0,
                "duration_hours": 2.0,
                "coords": [26.9258, 75.8236],
                "is_outdoor": False,
                "rating": 4.7
            },
            {
                "id": "jai_jantar",
                "name": "Jantar Mantar Astronomical Site",
                "description": "See the world's largest stone sundial and unique geometric star trackers.",
                "category": "culture",
                "cost": 3.0,
                "duration_hours": 1.5,
                "coords": [26.9248, 75.8245],
                "is_outdoor": True,
                "rating": 4.6
            },
            {
                "id": "jai_nahargarh",
                "name": "Nahargarh Fort Clifftop Sunset Walk",
                "description": "Overlook the entire pink city from the fortress walls as lights turn on.",
                "category": "adventure",
                "cost": 2.0,
                "duration_hours": 2.5,
                "coords": [26.9374, 75.8156],
                "is_outdoor": True,
                "rating": 4.8
            },
            {
                "id": "jai_bazaar",
                "name": "Johri Bazaar Rajasthani Street Food Crawl",
                "description": "Sample pyaz kachoris, lassis, and local sweet ghevar.",
                "category": "food",
                "cost": 5.0,
                "duration_hours": 2.0,
                "coords": [26.9189, 75.8288],
                "is_outdoor": True,
                "rating": 4.6
            },
            {
                "id": "jai_albert_hall",
                "name": "Albert Hall Central State Museum",
                "description": "Explore Rajasthani pottery, ivory designs, and an Egyptian mummy.",
                "category": "culture",
                "cost": 4.0,
                "duration_hours": 2.0,
                "coords": [26.9116, 75.8195],
                "is_outdoor": False,
                "rating": 4.6
            },
            {
                "id": "jai_chokhi_dhani",
                "name": "Chokhi Dhani Ethnic Resort Village Tour",
                "description": "Witness puppet shows, camel rides, folk dances, and eat a lavish Rajasthani thali.",
                "category": "food",
                "cost": 15.0,
                "duration_hours": 4.0,
                "coords": [26.7681, 75.8363],
                "is_outdoor": True,
                "rating": 4.7
            },
            {
                "id": "jai_jaigarh",
                "name": "Jaigarh Fort & Giant Cannon Exhibition",
                "description": "View the massive Jaivana cannon, arms vaults, and water reservoir networks.",
                "category": "culture",
                "cost": 2.0,
                "duration_hours": 2.0,
                "coords": [26.9808, 75.8458],
                "is_outdoor": True,
                "rating": 4.6
            },
            {
                "id": "jai_birla_temple",
                "name": "Birla Mandir White Marble Temple",
                "description": "Tranquil temple made of pristine white marble with stained glass windows.",
                "category": "relaxation",
                "cost": 0.0,
                "duration_hours": 1.0,
                "coords": [26.8920, 75.8155],
                "is_outdoor": True,
                "rating": 4.7
            }
        ]
    }
}

