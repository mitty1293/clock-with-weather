from app import app
from flask import render_template, Response
from call_api import call_api, gen_url
import json

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/test')
def test():
    url = gen_url()
    data = call_api(url)
    json_text = json.dumps(data, indent=4)
    print(json_text)
