from flask import Flask
from pymongo import MongoClient
import urllib


def create_app(package_name, package_path, settings_override=None):
    app = Flask(package_name, instance_relative_config=True, static_folder='static', static_url_path='')

    # Load config from file app/settings.py
    # For dev config choose 'app.settings.DevConfig'
    # For Test config choose 'app.settings.TestConfig'
    app.config.from_object('app.settings.DevConfig')

    # Load config from location specified in ENV
    app.config.from_envvar("KIGATA_SETTINGS", silent=True)

    # Override settings
    app.config.from_object(settings_override)

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
    mongo_server = app.config['MONGO_SERVER']
    mongo_port = app.config['MONGO_PORT']
    mongo_user = urllib.quote_plus(app.config['MONGO_USERNAME'])
    mongo_passwd = urllib.quote_plus(app.config['MONGO_PASSWORD'])
    mongo_db = app.config['MONGO_DBNAME']
    (connect_string) = ('mongodb://mongo_user:' + mongo_passwd + '@' +
                      mongo_server + '/' + str(mongo_port) + '/' + mongo_db)
    connection = MongoClient(connect_string)
    mongodb = connection[mongo_db]


def configure_mongodb2(app):
    app.logger.info('configure_mongodb2')
    global mongodb2
    mongo_server = app.config['MONGO_TEST1_SERVER']
    mongo_port = app.config['MONGO_TEST1_PORT']
    mongo_user = app.config['MONGO_TEST1_USERNAME']
    mongo_passwd = app.config['MONGO_TEST1_PASSWORD']
    mongo_db = app.config['MONGO_TEST1_DBNAME']
    (connect_string) = ("mongodb://" + mongo_user + ':' + mongo_passwd + '@' +
                      mongo_server + ':' + mongo_port + "/" + mongo_db)
    connection = MongoClient(connect_string)
    mongodb = connection[mongo_db]