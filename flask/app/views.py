from app import app
from flask import render_template, Response
from . import api, extract_data
import json

@app.route('/')
def index():
    weather_endpoint: str = api.gen_endpoint()
    all_weather_data: dict = api.call_api(weather_endpoint)
    current_data = extract_data.of_current(**all_weather_data)
    hourly_data = extract_data.of_hourly(**all_weather_data)
    return render_template("index.html")

@app.route('/test')
def test():
    endpoint: str = api.gen_endpoint()
    data: dict = api.call_api(endpoint)
    json_text: str = json.dumps(data, indent=4)
    print(json_text)
