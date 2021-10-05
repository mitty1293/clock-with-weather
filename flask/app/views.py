from app import app
from flask import render_template, Response
from . import api
import json

@app.route('/')
def index():
    weather_endpoint = api.gen_endpoint()
    weather_data = api.call_api(weather_endpoint)
    return render_template("index.html")

@app.route('/test')
def test():
    endpoint = api.gen_endpoint()
    data = api.call_api(endpoint)
    json_text = json.dumps(data, indent=4)
    print(json_text)
