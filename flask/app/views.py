from app import app
from flask import render_template, Response
from. import gen_url, call_api
import json

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/test')
def test():
    url = gen_url.gen_url()
    data = call_api.call_api(url)
    json_text = json.dumps(data, indent=4)
    print(json_text)
