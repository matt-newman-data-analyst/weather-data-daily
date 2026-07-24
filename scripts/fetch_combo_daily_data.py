"""
Fetch daily max temperature for a fixed set of locations, from a fixed
start date up to yesterday, and write the result to a JSON file.

Data source: Open-Meteo Historical Weather API (archive-api.open-meteo.com)
This endpoint is used (rather than the standard forecast endpoint) because
it is designed for actual observed data over a rolling historical window,
which is what we want for a "fixed start date -> yesterday" daily append job.

Output file is fully overwritten on each run with the complete date range
(2026-07-01 -> yesterday). This keeps the logic simple and avoids drift,
at the cost of re-fetching the whole range every day.
"""

import json
from datetime import date, timedelta
from pathlib import Path

import requests

# --- Config -----------------------------------------------------------

START_DATE = "2026-07-01"  # fixed start date, does not change

OUTPUT_PATH = Path("data/_combo_daily_append.json")

LOCATIONS = [
    {"name": "London", "latitude": 51.5, "longitude": -0.0},
    {"name": "Paris", "latitude": 49.0, "longitude": 2.0},
    {"name": "Rome", "latitude": 42.0, "longitude": 12.5},
    {"name": "Edinburgh", "latitude": 56.0, "longitude": -3.25},
    {"name": "Madrid", "latitude": 40.5, "longitude": -3.75},
    {"name": "Stockholm", "latitude": 59.25, "longitude": 18.0},
    {"name": "Berlin", "latitude": 52.5, "longitude": 13.5},
    {"name": "Dublin", "latitude": 53.5, "longitude": -6.25},
    {"name": "Lisbon", "latitude": 38.75, "longitude": -9.25},
    {"name": "Vienna", "latitude": 48.25, "longitude": 16.5},
    {"name": "Warsaw", "latitude": 52.25, "longitude": 21.0},
    {"name": "Oslo", "latitude": 60.0, "longitude": 10.75},
    {"name": "Bern", "latitude": 47.0, "longitude": 7.5},
    {"name": "Athens", "latitude": 38.0, "longitude": 23.75}
]

ARCHIVE_URL = "https://archive-api.open-meteo.com/v1/archive"

# --- Helpers ------------------------------------------------------------


def get_end_date() -> str:
    """Yesterday's date, as an ISO string (YYYY-MM-DD)."""
    return (date.today() - timedelta(days=1)).isoformat()


def fetch_all_locations(start_date: str, end_date: str) -> list[dict]:
    """
    Query all locations in a single Open-Meteo request using comma-separated
    latitude/longitude lists. Returns the raw list of per-location response
    objects as given back by the API (order matches the input order).
    """
    params = {
        "latitude": ",".join(str(loc["latitude"]) for loc in LOCATIONS),
        "longitude": ",".join(str(loc["longitude"]) for loc in LOCATIONS),
        "daily": "temperature_2m_max",
        "start_date": start_date,
        "end_date": end_date,
        "timezone": "auto",
    }

    response = requests.get(ARCHIVE_URL, params=params, timeout=30)
    response.raise_for_status()

    data = response.json()

    # If only one location is ever configured, Open-Meteo returns a single
    # object rather than a list. Normalise to a list either way.
    if isinstance(data, dict):
        data = [data]

    return data


def build_output(raw_results: list[dict]) -> list[dict]:
    """
    Combine the raw per-location API responses with our location names,
    and reshape into a flat list of {location, date, temperature_2m_max}
    records, which is easier to consume downstream than the API's native
    parallel-array format.
    """
    records = []

    for loc, result in zip(LOCATIONS, raw_results):
        daily = result.get("daily", {})
        dates = daily.get("time", [])
        max_temps = daily.get("temperature_2m_max", [])

        for day, temp in zip(dates, max_temps):
            records.append(
                {
                    "location": loc["name"],
                    "latitude": loc["latitude"],
                    "longitude": loc["longitude"],
                    "date": day,
                    "temperature_2m_max": temp,
                }
            )

    return records


def main() -> None:
    start_date = START_DATE
    end_date = get_end_date()

    print(f"Fetching daily max temperature from {start_date} to {end_date} "
          f"for {len(LOCATIONS)} location(s)...")

    raw_results = fetch_all_locations(start_date, end_date)
    records = build_output(raw_results)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("w") as f:
        json.dump(records, f, indent=2)

    print(f"Wrote {len(records)} records to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
