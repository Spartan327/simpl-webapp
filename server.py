from flask import Flask
from weather import weather_by_city

app = Flask(__name__)


@app.route('/')
def index():
    weather = weather_by_city("Krasnoyarsk,Russia")
    if weather:
        return f"Температура в городе Красноярск {weather['temp_C']} С,\
                 ощущается как {weather['FeelsLikeC']} С,\
                 ветер {weather['windspeedKmph']} км/ч."
    else:
        return "Сервис погоды временно недоступен"


if __name__ == "__main__":
    app.run(debug=True)
