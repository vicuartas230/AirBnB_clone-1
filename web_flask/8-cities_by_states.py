#!/usr/bin/python3
""" This script starts a Flask web application """
from models import storage
from flask import Flask, render_template
from models.state import State


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities():
    """ This function lists City objects linked to the State """
    return render_template("8-cities_by_states.html", cons=storage.all(State))


@app.teardown_appcontext
def teardown(exception):
    """ This function removes the current SQLAlchemy Session. """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
