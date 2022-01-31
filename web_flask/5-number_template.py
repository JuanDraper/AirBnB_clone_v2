#!/usr/bin/python3
""" will start flask """
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def croute(text):
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def Pythonroute(text):
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return str(n) + ' is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def numbertemp(n):
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
