#!/usr/bin/python3
""" script that starts a Flask web application using the Hbnb_clone data """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_storage(exception):
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def list_states_and_cities():
    states_list = storage.all(State)
    res = []
    for states_id, states in states_list.items():
            res.append({'id': states.id, 'name': states.name,
                        'cities': states.cities})
    print(res)
    return render_template('8-cities_by_states.html', states_lt=res)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
