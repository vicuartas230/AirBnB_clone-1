#!/usr/bin/python3
""" This script starts a Flask web application """
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def say_hello():
    """ This function says hello """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def print_b():
    """ This function prints HBNB """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def use_variable(text):
    """ This function prints c whit a variable """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def default_value(text='is cool'):
    """ This function uses a variable with default value. """
    return 'Python {}'.format(text.replace('_', ' '))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
