# Weather Information Script

This Python script allows you to fetch and display the current weather information for a given city using the OpenWeatherMap API.

## Features

- Fetches current weather data for a specified city.
- Displays temperature (in Celsius), atmospheric pressure, humidity, and weather description.

## Prerequisites

- Python 3.x
- `requests` library (can be installed via `pip install requests`)
- OpenWeatherMap API key

## Setup
1. **Install the required Python libraries**:

   ```bash
   pip install requests
   ```

2. **Obtain an API key**:

   - Sign up at [OpenWeatherMap](https://openweathermap.org/) if you don't have an account.
   - Go to the API keys section in your account settings.
   - Generate and copy your API key.

3. **Update the script with your API key**:

   Replace the placeholder API key in the script with your actual API key.

   ```python
   api_key = "your_openweathermap_api_key_here"
   ```

## Usage

1. **Run the script**:

   ```bash
   python weather.py
   ```

2. **Enter the name of the city**:

   When prompted, enter the name of the city for which you want to fetch the weather information.

## Script Details

```python
import requests

def get_weather_data(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    return response.json()

def kelvin_to_celsius(temp_kelvin):
    return temp_kelvin - 273.15

def print_weather_data(city_name, data):
    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]

        current_temperature_kelvin = main["temp"]
        current_temperature_celsius = kelvin_to_celsius(current_temperature_kelvin)

        current_pressure = main["pressure"]
        current_humidity = main["humidity"]
        weather_description = weather["description"]

        print(f"Weather in {city_name}:")
        print(f" Temperature: {current_temperature_celsius:.2f}°C")
        print(f" Atmospheric pressure: {current_pressure} hPa")
        print(f" Humidity: {current_humidity}%")
        print(f" Description: {weather_description.capitalize()}")
    else:
        print("City Not Found")

def main():
    api_key = "your_openweathermap_api_key_here"
    city_name = input("Enter city name: ").strip()

    if city_name:
        weather_data = get_weather_data(city_name, api_key)
        print_weather_data(city_name, weather_data)
    else:
        print("Please enter a valid city name.")

if __name__ == "__main__":
    main()
```

## Error Handling

- If the city is not found, the script will output "City Not Found".
- Ensure that you have a valid and activated API key from OpenWeatherMap.

