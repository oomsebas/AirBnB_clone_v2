#!/usr/bin/python3
""" script that starts a Flask web application using the Hbnb_clone data """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_storage(exception):
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    states_list = storage.all(State)
    res = []
    for key, states in states_list.items():
        res.append({'id': states.id, 'name': states.name})
    return render_template('9-states.html', states_lt=res)


@app.route('/states/<id>', strict_slashes=False)
def state_by_id(id):
    states_list = storage.all(State)
    res = []
    for key, states in states_list.items():
        if id == states.id:
            res.append({'id': states.id, 'name': states.name,
                        'cities': states.cities})
    return render_template('9-states.html', state_city=res)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
