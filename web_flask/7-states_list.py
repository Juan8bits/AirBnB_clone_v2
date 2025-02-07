#!/usr/bin/python3
""" Script that start flask. """
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def teardown():
    """ Handler for teardow"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list_page():
    """ Redirect to page with all states. """
    states = storage.all("State").values()
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
