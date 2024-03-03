# Weather Forecast API

## Introduction

The Weather Forecast API provides weather forecasts based on zip codes. It fetches weather data from the OpenWeatherMap API and implements caching to improve performance.

## Implementation Details

### Technologies Used

- **Language:** Python
- **Framework:** Flask
- **Weather API:** OpenWeatherMap

### Code Structure

The application consists of the following components:

1. **Main Application Code (`run.py`):**

   - Contains the Flask application setup.
   - Implements the `/weather` endpoint to fetch weather forecasts.
   - Includes caching mechanism to store and retrieve forecasts.

2. **Weather Forecast Function (`get_weather_forecast`):**

   - This function interacts with the OpenWeatherMap API to fetch weather data based on a given zip code.

3. **Caching Mechanism (`forecast_cache`):**
   - A dictionary that caches weather forecasts with zip codes as keys.
   - Each cache entry consists of the forecast data and the timestamp when it was cached.

### Endpoint Details

#### `/weather`

- **Method:** `GET`
- **Parameters:**
  - `zipcode`: The zip code for which weather forecast is requested.
- **Response:**
  - `forecast`: Object containing weather forecast data.
    - `temp`: Current temperature.
    - `temp_min`: Minimum temperature.
    - `temp_max`: Maximum temperature.
  - `from_cache`: Boolean indicating whether the result is pulled from cache.

### Caching

- The API caches weather forecasts for 30 minutes for subsequent requests with the same zip code.
- If the result is pulled from the cache, the `from_cache` field in the response is set to `True`.

## Usage Example and Conclusion

The Weather Forecast API provides a simple yet efficient way to fetch weather forecasts based on zip codes. By implementing caching, it ensures faster response times for subsequent requests with the same zip code.

### Usage Example

Request:

```
GET /weather?zipcode=10001
```

Response:

```json
{
  "forecast": {
    "temp": 20,
    "temp_min": 18,
    "temp_max": 22
  },
  "from_cache": false
}
```
