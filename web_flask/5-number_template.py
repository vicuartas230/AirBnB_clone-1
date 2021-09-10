#!/usr/bin/python3
""" This script starts a Flask web application """
from flask import Flask, render_template


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

    return f'C {text}'.replace('_', ' ')

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def default_value(text='is cool'):
    """ This function uses a variable with default value. """
    return f'Python {text}'.replace('_', ' ')

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ This function displays n if it is an integer """
    return f'{n} is a number'

@app.route('/number_template/<int:n>', strict_slashes=False)
def html_page(n):
    """ This function displays a HTML page if n is an integer. """
    return render_template("5-number.html", n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
