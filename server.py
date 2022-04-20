import requests
<<<<<<< HEAD
=======

>>>>>>> master
from flask import Flask, render_template
import os

API_KEY = os.environ["API_KEY"]
BASE_URL = os.environ.get("BASE_URL")
user_input = "helsinki"
LAT = 60.1699
LON = 24.9384

FLASK_APP = Flask(__name__, static_url_path="",
                  static_folder="web/static", template_folder="web/templates")
<<<<<<< HEAD
=======

>>>>>>> master

@FLASK_APP.route('/')

def hello_world():
<<<<<<< HEAD
    return render_template('index.html', message="Hello World! ")
=======

    return render_template('index.html', message="Hello World! ")

>>>>>>> master

@FLASK_APP.route('/current')

def current():
    try:
<<<<<<< HEAD
=======

>>>>>>> master
        r = requests.get(
            f'{BASE_URL}/weather?q={user_input}&units=metrics&appid={API_KEY}')
        r.raise_for_status()
        data = r.json()

        current_weather = {
            "description" : data["weather"][0]["description"].title(),
            "icon": data["weather"][0]["icon"],
            "name": data["name"],
            "temperature": data["main"]["temp"],
            "wind": data["wind"]["speed"]
        }

        return render_template("index.html", weather=current_weather)
    except requests.exceptions.HTTPError as err:
        return f"Error: {err}"

@FLASK_APP.route('/forecast')
def forecast():
<<<<<<< HEAD
=======

>>>>>>> master
    r = requests.get(f'{BASE_URL}/onecall?lat={LAT}&lon={LON}&units=metrics&appid={API_KEY}').json()
    return render_template("index.html", forecast= r["daily"])

@FLASK_APP.errorhandler(404)
<<<<<<< HEAD

=======
>>>>>>> master
def page_not_found(error):
    return render_template("index.html", message=error), 404


if __name__ == "__main__":
<<<<<<< HEAD

=======
>>>>>>> master
    port = int(os.environ.get("PORT", 5000))
    FLASK_APP.run(debug =  True, host="0.0.0.0", port = port)
