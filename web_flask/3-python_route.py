#!/usr/bin/python3
"""It starts a Flask web application
web application must be listening on 0.0.0.0, port 5000
Routes:

    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
    /python/<text>: display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
        The default value of text is “is cool”
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnb_route():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<string:text>', strict_slashes=False)
def c_text(text):
    text = text.replace("_", " ")
    return "C %s" % text


@app.route('/python', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python_text(text="is cool"):
    text = text.replace("_", " ")
    return "Python %s" % text


if __name__ == "__main__":
    app.run(host="0.0.0.0")
