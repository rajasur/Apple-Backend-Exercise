from app import app
import requests
from app import app
from config import Config
import time

def get_weather_forecast(zipcode):
    api_key = app.config['OPENWEATHERMAP_API_KEY']
    url = f"http://api.openweathermap.org/data/2.5/weather?zip={zipcode}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if 'main' in data:
        forecast = {
            'temp': data['main']['temp'],
            'temp_min': data['main']['temp_min'],
            'temp_max': data['main']['temp_max']
        }
        return forecast
    else:
        return None

def get_cached_forecast(zipcode):
    cache = app.config['CACHE']
    if zipcode in cache:
        timestamp, forecast = cache[zipcode]
        # Check if cache is not expired (30 minutes)
        if time.time() - timestamp <= 1800:  # 1800 seconds = 30 minutes
            return forecast, True  # Return cached forecast and indicator
        else:
            del cache[zipcode]  # Delete expired cache entry
    return None, False