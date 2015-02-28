#!/usr/bin/python

from app.resources import RestApiView
from flask import Flask

# WSGI needs to find 'application'
application = Flask(__name__)

# Register the resources below
RestApiView.register(application)

if __name__ == '__main__':
    application.run(
        debug=True,
        host='0.0.0.0',
        port=8080,
        )