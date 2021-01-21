#!/usr/bin/python3
""" use flask to display our hbnb project """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def teardown_storage(exception):
    """ tear down function """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """ implementation for the filters on hbnb webpage """
    states = storage.all(State)
    amen = storage.all(Amenity)
    return render_template('10-hbnb_filters.html', states_list=states,
                           amen_list=amen)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
