#!/usr/bin/python3
""" Script that starts a Flask web application with two diferents routes. """
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def First_page():
    """ Redirection for '/' route page. """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb_page():
    """ Redirection for '/hbnb' page. """
    return 'HBNB'


@app.route('/c/<text>')
def c_page(text):
    """ Redirection for '/c/ page and returning a variable. '"""
    text = text.replace("_", " ")
    return ('C {}'.format(text))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
