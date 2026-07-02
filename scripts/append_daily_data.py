import requests
import json
from datetime import date, timedelta

# === CONFIG ===
LATITUDE = "51.5"
LONGITUDE = "-0.0"
START_DATE = "2026-07-01"
OUTPUT_FILE = "daily_weather_append.json"

def get_end_date():
    """Yesterday = last fully complete day"""
    yesterday = date.today() - timedelta(days=1)
    return yesterday.isoformat()

def fetch_weather():
    end_date = get_end_date()
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": LATITUDE,
        "longitude": LONGITUDE,
        "start_date": START_DATE,
        "end_date": end_date,
        "daily": "temperature_2m_max",
        "timezone": "auto"
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    with open(OUTPUT_FILE, "w") as f:
        json.dump(data, f, indent=2)

    print(f"Saved data from {START_DATE} to {end_date} -> {OUTPUT_FILE}")

if __name__ == "__main__":
    fetch_weather()
