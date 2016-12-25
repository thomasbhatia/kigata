from flask import Flask
from app.contrib.middle_ware.request import after_request
from contrib.mongotalk import mongodb


def create_app(package_name, package_path, settings_override=None):
    app = Flask(package_name, instance_relative_config=True, static_folder='static', static_url_path='')

    # Load config from file app/settings.py
    # For dev config choose 'app.settings.DevConfig'
    # For Test config choose 'app.settings.TestConfig'
    app.config.from_object('app.settings.DevConfig')

    # Load config from location specified in ENV
    app.config.from_envvar("KIGATA_SETTINGS", silent=True)

    # Removes the trailing slash in the url on redirect
    app.url_map.strict_slashes = False

    # Override settings
    app.config.from_object(settings_override)

    configure(app)

    @app.after_request
    def after_requests(response):
        return after_request(response)

    return app


def configure(app):
    # initialise mongodb connection.
    configure_mongodb(app)


def configure_mongodb(app):
    mongodb.init_app(app)
