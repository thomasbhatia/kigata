#!/usr/bin/python

from app.resources import RestApiView
from flask import Flask

# WSGI needs to find 'application'
application = Flask(__name__)
application.config.from_object('app.settings.Config')

# Register the resources below
RestApiView.register(application)

if __name__ == '__main__':
    application.run(
        debug=application.config['DEBUG'],
        host=application.config['HOST'],
        port=application.config['PORT'],
        )