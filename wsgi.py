#!/usr/bin/python

# Preserve the order of imports here!
from app import create_app
from app.resources import RestApiView

# WSGI needs to find 'application'
application = create_app()

# Register the resources below
RestApiView.register(application)

if __name__ == '__main__':
    application.run(
        host=application.config['HOST'],
        )