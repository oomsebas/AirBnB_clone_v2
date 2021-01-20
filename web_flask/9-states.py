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
    res = []
    if id:
        states1 = None
        for key, states in states_list.items():
            if id == states.id:
                states1 = states
                break
        return render_template('9-states.html', state_city=states1)
    else:
        for key, states in states_list.items():
            res.append({'id': states.id, 'name': states.name})
        return render_template('9-states.html', states_lt=res)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
