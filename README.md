# weather-data-daily
weather data test

##london uses greenwich
https://archive-api.open-meteo.com/v1/archive?latitude=51.5&longitude=-0.0&start_date=2026-01-01&end_date=2026-06-30&daily=temperature_2m_max&timezone=auto

##paris uses versailles
https://archive-api.open-meteo.com/v1/archive?latitude=49.0&longitude=2.0&start_date=1940-01-01&end_date=1979-12-31&daily=temperature_2m_max&timezone=auto

##rome is just a few miles north of rome
https://archive-api.open-meteo.com/v1/archive?latitude=42.0&longitude=12.5&start_date=1940-01-01&end_date=2026-06-30&daily=temperature_2m_max&timezone=auto

##edinburgh
https://archive-api.open-meteo.com/v1/archive?latitude=56.0&longitude=-3.25&start_date=1940-01-01&end_date=2026-06-30&daily=temperature_2m_max&timezone=auto

##madrid
https://archive-api.open-meteo.com/v1/archive?latitude=40.5&longitude=-3.75&start_date=1940-01-01&end_date=2026-06-30&daily=temperature_2m_max&timezone=auto

##stockholm
https://archive-api.open-meteo.com/v1/archive?latitude=59.25&longitude=18.0&start_date=1940-01-01&end_date=2026-06-30&daily=temperature_2m_max&timezone=auto

##berlin
https://archive-api.open-meteo.com/v1/archive?latitude=52.5&longitude=13.5&start_date=1940-01-01&end_date=2026-06-30&daily=temperature_2m_max&timezone=auto

##athens
https://archive-api.open-meteo.com/v1/archive?latitude=38.0&longitude=23.75&start_date=1940-01-01&end_date=2026-06-30&daily=temperature_2m_max&timezone=auto

##other lat longs (taken from .py file)
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


###
daily updates with multiple geos
https://api.open-meteo.com/v1/forecast?latitude=51.05,53.48,52.52&longitude=-1.80,-2.24,13.41&daily=temperature_2m_max&timezone=auto
##amended to use py and yml

