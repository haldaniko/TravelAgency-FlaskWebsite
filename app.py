from flask import Flask, render_template
import sqlite3
app = Flask(__name__)


def create_dict_from_table():
    conn = sqlite3.connect('tours.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tour')
    data = cursor.fetchall()
    tours = {}
    for row in data:
        tour = {}
        tour['title'] = row[2]
        tour['description'] = row[3]
        tour['departure'] = row[4]
        tour['picture'] = row[5]
        tour['stars'] = int(row[6])
        tour['country'] = row[7]
        tour['nights'] = row[8]
        tour['date'] = row[9]
        tours[row[1]] = tour
    cursor.close()
    conn.close()
    return tours


tours = create_dict_from_table()
departures = {"berlin": "Berlin",
              "munich": "München",
              "hamburg": "Hamburg",
              "dusseldorf": "Düsseldorf",
              "frankfurt": "Frankfurt"}


@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html",
                           tours=tours,
                           departures=departures)


@app.route("/departure/<city>/")
def departure(city):
    if city in departures.keys():
        return render_template("departure.html",
                               departures=departures,
                               tours=tours,
                               city=city)


@app.route("/tours/<tour_title>/")
def tour(tour_title):
    if tour_title in tours.keys():
        return render_template("tour.html",
                               departures=departures,
                               tours=tours,
                               tour_title=tour_title)


app.run()
