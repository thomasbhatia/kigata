#!/usr/bin/python
import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PROJECT_ROOT)

# Activates the virtualenv environment
activate_this = PROJECT_ROOT+'/.env/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

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
