#!/usr/bin/python3
""" will start flask"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_and_var(text):
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def Python_and_var(text):
    return 'Python ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
