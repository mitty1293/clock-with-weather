#!/usr/bin/python3
# _*_ coding: utf-8 _*_

import requests, json
from requests.models import Response

def call_api(url: str) -> str:
    response: Response = requests.get(url)
    json_data: dict = response.json()
    json_text: str = json.dumps(json_data, indent=4)
    return json_text
