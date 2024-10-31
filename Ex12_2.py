# Ex12_2.py

import requests


def get_weather(city, api_key):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()

        # Extract weather description and temperature
        weather_description = data["weather"][0]["description"]
        temperature_kelvin = data["main"]["temp"]
        temperature_celsius = temperature_kelvin - 273.15  # Convert Kelvin to Celsius

        # Display the results
        print(f"Weather in {city.capitalize()}: {weather_description}")
        print(f"Temperature: {temperature_celsius:.2f}°C")
    except requests.exceptions.RequestException as e:
        print("Error fetching weather data:", e)
    except KeyError:
        print("Invalid city name or data not available.")


if __name__ == "__main__":
    api_key = "a389ea4b1b8795cadf55490b8a74bc65"  # Use the actual OpenWeather API key
    city = input("Enter the city name: ")
    get_weather(city, api_key)
