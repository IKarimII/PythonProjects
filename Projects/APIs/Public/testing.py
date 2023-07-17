import requests

API_KEY = '09b0afdb5faede2fb46ee409a75a0e3f'

parameters = {
    'lat': 34.119883,
    'lon': 35.650088,
    'appid': API_KEY
}
connection = requests.get(url='https://api.openweathermap.org/data/2.5/weather', params=parameters)
connection.raise_for_status()
data = connection.json()
print(data)