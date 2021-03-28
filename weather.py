import requests


def weather_by_city(city_name):
    weather_url = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
    params = {
        "key": "fd11f788d42640818ea41946212502",
        "q": city_name,
        "num_of_days": 1,
        "format": "json",
        "lang": "ru",
    }
    result = requests.get(weather_url, params=params)
    weather = result.json()
    if 'data' in weather:
        if 'current_condition' in weather['data']:
            try:
                return weather['data']['current_condition'][0]
            except(IndexError, TypeError):
                return False
    return False


if __name__ == "__main__":
    w = weather_by_city("Krasnoyarsk,Russia")
    print(w)
