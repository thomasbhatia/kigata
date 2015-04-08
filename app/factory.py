from flask import Flask
from flask.ext.pymongo import PyMongo


def create_app(package_name, package_path, settings_override=None):
    app = Flask(package_name, instance_relative_config=True, static_folder='static', static_url_path='')

    # Load config from file app/settings.py
    app.config.from_object('app.settings.Config')

    # APP secret key
    #app.secret_key = '\xa7\xf11Y\xfa`\xd9\xe8f\x94\x00w\x01n\xa2\xe1\xb2\x9d\x00\xf6o\x1b\x17U'

    configure(app)   

    @app.after_request
    def after(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Methods',
                             'POST, GET, PUT, PATCH, DELETE, OPTIONS')
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type, X-Requested-With, Authorization, X-HTTP-Method-Override')
        response.headers.add('Access-Control-Max-Age', '1728000')

        """
        Add headers to both force latest IE rendering engine or Chrome Frame
        """
        response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
        response.headers['Cache-Control'] = 'public, max-age=0'
        response.headers.add('Cache-Control', 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0')

        return response

    return app

def configure(app):
    # initialise mongodb connection.
    configure_mongodb(app)

    # Uncomment following line to initialise second mongodb connection.
    # configure_mongodb2(app) 

def configure_mongodb(app):
    app.logger.info('configure_mongodb')
    global mongodb
    mongodb = PyMongo()
    mongodb.init_app(app, config_prefix=app.config['MONGO_PREFIX'])

def configure_mongodb2(app):
    app.logger.info('configure_mongodb2')
    global mongodb2
    mongodb2 = PyMongo()
    mongodb2.init_app(app, config_prefix=app.config['MONGO2_PREFIX'])