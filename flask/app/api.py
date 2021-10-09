#!/usr/bin/python3
# _*_ coding: utf-8 _*_

import requests
import configparser
from requests.models import Response

def gen_endpoint() -> str:
    config = configparser.ConfigParser()
    config.read('/run/secrets/weather_secrets')
    url: str = "https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units=metric&appid={key}"
    endpoint: str = url.format(key=config['API']['KEY'], lat=config['coordinates']['LAT'], lon=config['coordinates']['LON'])
    return endpoint

def call_api(endpoint: str) -> dict:
    res_as_json: Response = requests.get(endpoint)
    res_as_dict: dict = res_as_json.json()
    return res_as_dict
