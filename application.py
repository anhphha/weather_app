import requests
from flask import Flask, render_template
import os

API_KEY = os.environ["API_KEY"]
BASE_URL = os.environ.get("BASE_URL")
user_input = "helsinki"
LAT = 60.1699
LON = 24.9384

application=Flask(__name__, static_url_path="",
                  static_folder="web/static", template_folder="web/templates")

@application.route('/')

def hello_world():
<<<<<<< HEAD:server.py
    return render_template('index.html', message="5 Day Weather Forecast")
=======
    return render_template('index.html', message="Hello World! ")
>>>>>>> master:application.py

@application.route('/current')

def current():
    try:
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

<<<<<<< HEAD:server.py
@FLASK_APP.route('/forecast')
=======
@application.route('/forecast')
>>>>>>> master:application.py

def forecast():
    r = requests.get(f'{BASE_URL}/onecall?lat={LAT}&lon={LON}&units=metrics&appid={API_KEY}').json()
    return render_template("index.html", forecast= r["daily"])

<<<<<<< HEAD:server.py
@FLASK_APP.errorhandler(404)
=======
@application.errorhandler(404)
>>>>>>> master:application.py

def page_not_found(error):
    return render_template("index.html", message=error), 404


if __name__ == "__main__":
<<<<<<< HEAD:server.py
   port = int(os.environ.get("PORT", 5000))
   FLASK_APP.run(debug =  True, host="0.0.0.0", port = port)
=======
    port = int(os.environ.get("PORT", 5000))
    application.run(debug =  True, host="0.0.0.0", port = port)
>>>>>>> master:application.py
