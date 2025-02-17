#!/usr/bin/python3
""" This script starts a Flask web application """
from models import storage
from flask import Flask, render_template
from models.state import State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ This function lists of all State objects present in DBStorage """
    return render_template("7-states_list.html", cons=storage.all(State))


@app.teardown_appcontext
def teardown(exception):
    """ This function removes the current SQLAlchemy Session. """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
