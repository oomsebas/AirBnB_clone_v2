#!/usr/bin/python3
""" script that starts a Flask web application using the Hbnb_clone data """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_storage(exception):
    """ tear down function """
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """state and cities render"""
    states_list = storage.all(State)
    res = None
    states1 = None
    if id:
        if 'State.' + id in states_list:
            states1 = states_list.get('State.' + id)
    else:
        res = states_list
    return render_template('9-states.html', states_lt=res,
                           state_city=states1, id=id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
