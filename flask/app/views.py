from app import app
from flask import render_template, Response
from . import api, extract_data
import json

@app.route('/')
def index():
    weather_endpoint: str = api.gen_endpoint()
    all_weather_data: dict = api.call_api(weather_endpoint)
    hourly_data: list = extract_data.of_hourly(**all_weather_data)
    daily_data: list = extract_data.of_daily(**all_weather_data)
    return render_template("index.html", hourly_data=hourly_data)

@app.route('/test')
def test():
    endpoint: str = api.gen_endpoint()
    data: dict = api.call_api(endpoint)
    json_text: str = json.dumps(data, indent=4)
    print(json_text)
