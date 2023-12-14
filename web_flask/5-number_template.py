#!/usr/bin/python3

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!\n"
	
@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB!\n"

@app.route("/c/<text>", strict_slashes=False)
def displaytext(text):
		return f"c {text.replace('_', ' ')}\n"

@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", strict_slashes=False)
def displayPythonText(text='is_cool'):
		return f"python {text.replace('_', ' ')}\n"

@app.route("/number/<int:n>", strict_slashes=False)
def displayNumber(n):
			return f"{n} is a number\n"

@app.route("/number_template/<int:n>", strict_slashes=False)
def displayNumberTemplate(n):
			return render_template('5-number.html', n=n)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000, debug=True )
