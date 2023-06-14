import json

from flask import Flask, render_template, redirect
import requests
from settings import settings

app = Flask(__name__)

key = settings.get("API_KEY")
pexels_key = settings.get("PEXELS_KEY")
q = settings.get("location", "NewYork")
lang = settings.get("language", "en")
system = settings.get("system", "metric")

symbols = {
    "temp": "wi-celsius",
    "temp_key": "temp_c",
    "feelslike": "feelslike_c",
    "velocity": "km/h",
    "velocity_key": "kph",
    "wind_key": "wind_kph",
    "pressure": "mb",
    "precip": "mm",
    "visibility": "km",
}

if system == "imperial":
    symbols["temp"] = "wi-fahrenheit"
    symbols["temp_key"] = "temp_f"
    symbols["feelslike"] = "feelslike_f"
    symbols["velocity"] = "mph"
    symbols["velocity_key"] = "mph"
    symbols["wind_key"] = "wind_mph"
    symbols["pressure"] = "in"
    system["precip"] = "in"
    system["visibility"] = "miles"

conditions = requests.get("https://www.weatherapi.com/docs/conditions.json")
conditions = conditions.content.decode('utf-8-sig')
conditions = json.loads(conditions)


def get_pexels(query: str):
    headers = {
        "Authorization": pexels_key
    }
    resp = requests.get(
        f"https://api.pexels.com/v1/search?query={query}&per_page=1&orientation=landscape",
        headers=headers
    )
    resp = resp.json()

    print(resp)
    return resp


def first(iterable, default=None):
    for item in iterable:
        return item
    return default


def get_icon_id(code):
    return first(x for x in conditions if x.code == code)["icon"] or ""


@app.route('/')
def hello_world():
    url = f"https://api.weatherapi.com/v1/forecast.json?key={key}&q={q}&lang={lang}"
    resp = requests.get(url)
    data = resp.json()

    if "error" in data:
        return data

    image = get_pexels(f"{data['current']['condition']['text']} nature weather")

    return render_template("base.html", data=data, symbols=symbols, url=url, image=image)


if __name__ == '__main__':
    app.run()
