import requests


def get_weather(city_name, api_key):
    """Fetch weather data for a given city using OpenWeatherMap API."""
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raises HTTPError for bad responses
        data = response.json()
        weather_info = {
            'description': data['weather'][0]['description'].capitalize(),
            'temperature': data['main']['temp'],
            'feels_like': data['main']['feels_like'],
            'humidity': data['main']['humidity']
        }
        return weather_info
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None


def display_weather(city_name, weather_info):
    """Print weather information in a user-friendly format."""
    if weather_info:
        print(f"Weather in {city_name}: {weather_info['description']}")
        print(f"Current Temperature: {weather_info['temperature']}°C")
        print(f"Feels Like: {weather_info['feels_like']}°C")
        print(f"Humidity: {weather_info['humidity']}%")
    else:
        print("Failed to retrieve weather data.")


def main():
    city_name = 'Agra'
    api_key = 'your API here..Please!'  # Update your openweathermap API key here

    weather_info = get_weather(city_name, api_key)
    display_weather(city_name, weather_info)


if __name__ == "__main__":
    main()
