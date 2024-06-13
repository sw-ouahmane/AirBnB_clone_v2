#!/usr/bin/python3
"""
Starts a Flask web application
"""

from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'

@app.route('/airbnb-onepage/', strict_slashes=False)
def airbnb_onepage():
    """returns Hello HBNB! at the /airbnb-onepage/ route"""
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

