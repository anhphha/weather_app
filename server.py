import requests
from flask import Flask
import os

API_KEY = os.environ["API_KEY"]
BASE_URL = "https://api.openweathermap.org/data/2.5/"
user_input = input("Enter city: ")
LAT = 60.1699
LON = 24.9384

FLASK_APP = Flask(__name__)

@FLASK_APP.route('/')

def hello_world():
    return '<p>Hello World!</p>'

@FLASK_APP.route('/current')

def current():
    try:
        r = requests.get(f'{BASE_URL}/weather?q={user_input}&appid={API_KEY}')
        r.raise_for_status()
        return r.json()
    except requests.exceptions.HTTPError as err:
        return f"Error: {err}"

@FLASK_APP.route('/forecast')

def forecast():
    return requests.get(f'{BASE_URL}/onecall?lat={LAT}&lon={LON}&appid={API_KEY}').json()
