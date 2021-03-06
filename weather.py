import requests
import config

API_KEY = config.api_key
BASE_URL = config.api_url

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    print(weather)
    temperature = data['main']['temp'] - 273.15
    fahrenheit = round(temperature*(9/5) + 32)
    print('Weather: ', weather)
    print("Temperature: ", fahrenheit, "F")
else:
    print("An error occurred")
