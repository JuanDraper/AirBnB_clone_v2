#!/usr/bin/python3
""" will star flask"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def teardownApp(self):
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def citiesStates():
    return render_template('8-cities_by_states.html',
                           states=storage.all("State"))


if __name__ == '__main__':
    app.run('0.0.0.0')
