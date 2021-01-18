#!/usr/bin/python3
""" display “C ” followed by the value of the text variable
    (replace underscore _ symbols with a space """

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


@app.route('/c/<append>', strict_slashes=False)
def c_append(append):
        """ return c plus the variable spaces"""
        spaces = append.replace("_", " ")
        return 'C {}'.format(spaces)

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
