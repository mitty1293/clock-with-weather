from app import app
from flask import render_template, Response

@app.route('/')
def index():
    return render_template("index.html")