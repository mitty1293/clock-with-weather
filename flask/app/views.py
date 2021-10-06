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
    # ↑ここまで完成。時間データと日データを取得できた。
    # ↓index.htmlを記載、時間データと日データを埋める箇所を作って、renderでhtmlに渡す。
    return render_template("index.html")

@app.route('/test')
def test():
    endpoint: str = api.gen_endpoint()
    data: dict = api.call_api(endpoint)
    json_text: str = json.dumps(data, indent=4)
    print(json_text)
