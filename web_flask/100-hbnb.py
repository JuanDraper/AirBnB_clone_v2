#!/usr/bin/python3
""" will start flask """
from flask import Flask
from flask import render_template
from models import storage
app = Flask(__name__)


@app.route('/states', strict_slashes=False, defaults={'id': None})
@app.route('/states/<id>', strict_slashes=False)
def slist(id):
    return render_template('9-states.html', states=storage.all("State"),
                           id=id)


@app.teardown_appcontext
def teardownApp(Error):
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def citiesStates():
    return render_template('8-cities_by_states.html',
                           states=storage.all("State"))


@app.route('/hbnb_filters', strict_slashes=False)
def hbnbFilters():
    return render_template('10-hbnb_filters.html', states=storage.all("State"),
                           amenities=storage.all("Amenity"))


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return render_template('100-hbnb.html', states=storage.all("State"),
                           amenities=storage.all("Amenity"),
                           places=storage.all("Place"))


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
