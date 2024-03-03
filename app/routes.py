from flask import jsonify, request
from app import app
from app.weather import get_weather_forecast, get_cached_forecast
import time

@app.route('/weather', methods=['GET'])
def weather_forecast():
    zipcode = request.args.get('zipcode')
    if not zipcode:
        return jsonify({'error': 'Zipcode parameter is missing'}), 400

    cached_forecast, from_cache = get_cached_forecast(zipcode)
    if cached_forecast:
        return jsonify({'forecast': cached_forecast, 'from_cache': from_cache})

    weather_forecast = get_weather_forecast(zipcode)
    if weather_forecast:
        return jsonify({'forecast': weather_forecast, 'from_cache': False})
    else:
        return jsonify({'error': 'Failed to fetch weather forecast for the given zipcode'}), 500