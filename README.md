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

   - Sign up at [OpenWeatherMap](https://openweathermap.org/) .
   - Go to the API keys section in your account settings.
   - Generate and copy your API key.

3. **Update the script with your API key**:

   Replace the placeholder API key in the script with your actual API key.


## Usage

1. **Run the script**:

   ```bash
   python weather.py
   ```

2. **Enter the name of the city**:

   When prompted, enter the name of the city for which you want to fetch the weather information.


## Error Handling

- If the city is not found, the script will output "City Not Found".
- Ensure that you have a valid and activated API key from OpenWeatherMap.

