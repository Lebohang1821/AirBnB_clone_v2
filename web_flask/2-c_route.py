#!/usr/bin/python3
"""It starts Flask web app"
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnb_route():
    """prints Hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """prints HBNB"""
    return "HBNB"


@app.route('/c/<string:text>', strict_slashes=False)
def c_text(text):
    un_text = un_text.replace("_", " ")
    return "C %s" % un_text


if __name__ == "__main__":
    app.run(host="0.0.0.0")
