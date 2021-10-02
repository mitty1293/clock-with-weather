#!/usr/bin/python3
# _*_ coding: utf-8 _*_

import requests
from requests.models import Response

def call_api(url: str) -> str:
    response: Response = requests.get(url)
    json_data: dict = response.json()
    return json_data
