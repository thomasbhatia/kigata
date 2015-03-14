from . import factory
from flask import jsonify


def create_app(settings_override=None):
    #Returns the app API application instance#

    app = factory.create_app(__name__, __path__, settings_override)

    #Removes the trailing slash in the url on redirect
    app.url_map.strict_slashes = False

    return app


