import os

import requests


def weather_search(town_name: str = "2112518") -> int:
    OPEN_WEATHER_KEY = os.environ['Weather_Key']
    URL = f'http://api.openweathermap.org/data/2.5/weather?id={town_name}&APPID={OPEN_WEATHER_KEY}'
    r = requests.get(URL).json()['weather'][0]['id']
    return r
