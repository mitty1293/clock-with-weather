#!/usr/bin/python3
# _*_ coding: utf-8 _*_

import requests, json

def call_api(url):
    response = requests.get(url)
    json_data = response.json()
    json_text = json.dumps(json_data, indent=4)
    print(json_text)
    return json_text
