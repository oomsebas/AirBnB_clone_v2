#!/usr/bin/python3
""" script that starts a Flask web application using the Hbnb_clone data """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_storage(exception):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def list_states():
    states_list = storage.all(State)
    res = {}
    for states in states_list.values():
        res[states.name] = {'id': states.id, 'name': states.name}
    return render_template('7-states_list.html', states_lt=res)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
