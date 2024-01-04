#!/usr/bin/python3

"""
Starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Returns Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def displaytext(text):
    """Display “C” followed by the value of the text variable"""
    return f"c {text.replace('_', ' ')}"


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", strict_slashes=False)
def displayPythonText(text='is cool'):
    """Display “Python”, followed by the value of the text variable"""
    return f"Python {text.replace('_', ' ')}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
