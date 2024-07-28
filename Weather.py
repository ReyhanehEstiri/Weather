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
    api_key = "a233d4ff15b20ac7fab0ffae4f8448ba"
    city_name = input("Enter city name: ").strip()

    if city_name:
        weather_data = get_weather_data(city_name, api_key)
        print_weather_data(city_name, weather_data)
    else:
        print("Please enter a valid city name.")

if __name__ == "__main__":
    main()
