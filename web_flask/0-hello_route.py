#!/usr/bin/python3

"""This module print the message Hello·HBNB"""
from flask import Flask


app = Flask(__name__)

"""Return the message"""
@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
