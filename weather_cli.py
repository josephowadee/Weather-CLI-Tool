"""
Weather CLI Tool 🌤

Python command-line interface (CLI) tool to fetch current weather data for any city
using the OpenWeatherMap API.

Author: Joseph
GitHub: https://github.com/josephowadee/Weather-CLI-Tool/tree/main

Usage:
    python weather_cli.py "New York"

Dependencies:
    - requests

Setup:
    1. Sign up at https://openweathermap.org/ to get a free API key.
    2. Replace 'YOUR_API_KEY' below with your actual API key.

"""

import sys
import requests

API_KEY = "YOUR_API_KEY"  # ← Replace this with your actual API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """Fetches weather data for a given city from OpenWeatherMap API."""
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code != 200:
        return f"Error: {data.get('message', 'Failed to fetch weather data.')}"
    
    weather = data['weather'][0]['description']
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    return f"{city.title()}: {weather}, 🌡️ {temp}°C (feels like {feels_like}°C)"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python weather_cli.py [city]")
    else:
        city = " ".join(sys.argv[1:])
        print(get_weather(city))