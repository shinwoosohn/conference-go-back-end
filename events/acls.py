from .keys import PEXELS_API_KEY, OPEN_WEATHER_API_KEY
import json
import requests


def get_photo(city, state):
    url = "https://api.pexels.com/v1/search"
    headers = {"Authorization": PEXELS_API_KEY}
    params = {
        "per_page": 1,
        "query": city + " " + state,
    }
    response = requests.get(url, headers=headers, params=params)
    content = json.loads(response.content)
    try:
        return {"picture_url": content["photos"][0]["src"]["original"]}
    except:
        return {"picture_url": None}


def get_weather_data(city, state):
    url = "http://api.openweathermap.org/geo/1.0/direct"
    headers = {"Authorization": OPEN_WEATHER_API_KEY}
    params = {
        "q": city + "," + state + ",USA",
        "appid": OPEN_WEATHER_API_KEY,
        "limit": 1,
    }
    response = requests.get(url, headers=headers, params=params)

    weather = json.loads(response.content)

    # print("\n----------", weather)
    try:
        w_lat = weather[0]["lat"]
        w_lon = weather[0]["lon"]
    except:
        return {
            "temp": None,
            "weather_description": None,
        }

    url2 = "https://api.openweathermap.org/data/2.5/weather"
    headers = {"Authorization": OPEN_WEATHER_API_KEY}
    params = {
        "lat": w_lat,
        "lon": w_lon,
        "appid": OPEN_WEATHER_API_KEY,
        "units": "imperial",
    }
    response2 = requests.get(url2, headers=headers, params=params)
    weather2 = json.loads(response2.content)
    weather_data = {
        "temp": weather2["main"]["temp"],
        "weather_description": weather2["weather"][0]["description"],
    }

    return weather_data
    #     return {
    #         "temp": weather2["main"]["temp"],
    #         "description": weather2["weather"][0]["description"],
    #     }
    # except:
    #     return {"temp": None, "description": None}
