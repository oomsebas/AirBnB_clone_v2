#!/usr/bin/python3
""" creates two route archives for the same host """

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
        """route 1"""
        return 'Hello, HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
        """ Route 2"""
        return 'HBNB'

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
