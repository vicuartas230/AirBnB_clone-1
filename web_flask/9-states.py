#!/usr/bin/python3
""" This script starts a Flask web application """
from models import storage
from flask import Flask, render_template
from models.state import State


app = Flask(__name__)


@app.route('/states')
def states():
    """ This function lists all State objects present in DBStorage """
    return render_template("9-states.html", cons=storage.all(State), id=None)


@app.route('/states/<id>')
def states_id(id):
    """ This function lists City objects linked to the state """
    query = [state for state in storage.all(State).values() if state.id == id]
    if query:
        return render_template("9-states.html", cons=query[0], id=id)
    else:
        return render_template("9-states.html", cons=None, id=id)


@app.teardown_appcontext
def teardown(exception):
    """ This function removes the current SQLAlchemy Session. """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
