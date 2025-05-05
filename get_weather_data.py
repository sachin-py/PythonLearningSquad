import requests

# Define the city and your OpenWeatherMap API key
city_name = 'Agra'
API_Key = 'abcD10862084123456eb8aefbb562ec9'  # Update your API here

# Construct the API request URL with city, API key, and metric units
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_Key}&units=metric'

# Send a GET request to the OpenWeatherMap API
response = requests.get(url)

# Check if the response was successful (HTTP status code 200)
if response.status_code == 200:
    # Parse the JSON response into a Python dictionary
    data = response.json()

    # Extract and print weather description
    print('Weather is', data['weather'][0]['description'])

    # Extract and print current temperature in Celsius
    print('Current Temperature is', data['main']['temp'])

    # Extract and print "feels like" temperature in Celsius
    print('Current Temperature Feels like is', data['main']['feels_like'])

    # Extract and print humidity percentage
    print('Humidity is', data['main']['humidity'])
else:
    # Print the HTTP error status code if the request failed
    print(f'Response code is {response.status_code}')
