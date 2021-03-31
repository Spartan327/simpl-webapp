from flask import Flask, render_template

from readmanga_top_week import get_top5_manga_week
from weather import weather_by_city

app = Flask(__name__)


@app.route('/')
def index():
    title = "Изучаем Python!"
    weather = weather_by_city("Krasnoyarsk,Russia")
    top5_manga_week = get_top5_manga_week()
    return render_template('index.html', title=title, weather=weather, top5_manga_week=top5_manga_week)


if __name__ == "__main__":
    app.run(debug=True)
