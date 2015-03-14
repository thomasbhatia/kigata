from flask import Flask
from flask.ext.pymongo import PyMongo


def create_app(package_name, package_path, settings_override=None):
    app = Flask(package_name, instance_relative_config=True, static_folder='static', static_url_path='')

    # Load config from file app/settings.py
    app.config.from_object('app.settings.Config')

    # APP secret key
    #app.secret_key = '\xa7\xf11Y\xfa`\xd9\xe8f\x94\x00w\x01n\xa2\xe1\xb2\x9d\x00\xf6o\x1b\x17U'

    global mongodb
    mongodb = PyMongo()
    mongodb.init_app(app)    

    return app
