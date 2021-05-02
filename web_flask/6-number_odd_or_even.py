#!/usr/bin/python3
""" Script that starts a Flask web application with two diferents routes. """
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False
# Also, we can define stric_slashes for specific redirection inside app.route()


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
    """ Redirection for '/c/ page and return a variable. """
    text = text.replace("_", " ")
    return ('C {}'.format(text))


@app.route('/python')
@app.route('/python/<text>')
def python_page(text='is cool'):
    """ Redirection for /python/ page an return a variable. """
    return ('Python {}'.format(text.replace("_", " ")))


@app.route('/number/<int:n>')
def number_page(n):
    """ Redirection for /number/ page and return a number
        only if is integer.
    """
    return ('{} is a number'.format(n))


@app.route('/number_template/<int:n>')
def number_template(n):
    """ Redirection for /number_template page and return HTML with a number
        only if is integer.
    """
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_even(n):
    """ Redirection for /number_odd_even page and return HTML with a number
        only if is integer.
    """
    text = " is odd"
    if n % 2 == 0:
        text = " is even"
    return render_template('6-number_odd_or_even.html', string=str(n)+text)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
