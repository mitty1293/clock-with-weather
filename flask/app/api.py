#!/usr/bin/python3
# _*_ coding: utf-8 _*_

import requests
from requests.models import Response
from . import keys

def gen_endpoint() -> str:
    url: str = "https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units=metric&appid={key}"
    endpoint: str = url.format(key=keys.API_KEY, lat=keys.LAT, lon=keys.LON)
    return endpoint

def call_api(endpoint: str) -> str:
    response: Response = requests.get(endpoint)
    json_data: dict = response.json()
    return json_data
