#!/usr/bin/python3
# _*_ coding: utf-8 _*_

import json
import requests
from requests.models import Response
from . import keys

def gen_endpoint() -> str:
    url: str = "https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units=metric&appid={key}"
    endpoint: str = url.format(key=keys.API_KEY, lat=keys.LAT, lon=keys.LON)
    return endpoint

def call_api(endpoint: str) -> dict:
    res_as_json: Response = requests.get(endpoint)
    res_as_dict: dict = res_as_json.json()
    return res_as_dict
