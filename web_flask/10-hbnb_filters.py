#!/usr/bin/python3
""" This script starts a Flask web application """
from models import storage
from flask import Flask, render_template
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """ This function displays a HTML page. """
    cons = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template("10-hbnb_filters.html", cons=cons, amenities=amenities)


@app.teardown_appcontext
def teardown(exception):
    """ This function removes the current SQLAlchemy Session. """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
