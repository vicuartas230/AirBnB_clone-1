#!/usr/bin/python3
""" This script starts a Flask web application """
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def say_hello():
    """ This function says hello """
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
