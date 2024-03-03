import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_weather_forecast_missing_zipcode(client):
    response = client.get('/weather')
    assert response.status_code == 400

def test_weather_forecast_invalid_zipcode(client):
    response = client.get('/weather?zipcode=abc123')
    assert response.status_code == 500

def test_weather_forecast_valid_zipcode(client):
    response = client.get('/weather?zipcode=10001')
    data = response.get_json()
    assert response.status_code == 200
    assert 'forecast' in data
    assert 'temp' in data['forecast']
    assert 'temp_min' in data['forecast']
    assert 'temp_max' in data['forecast']