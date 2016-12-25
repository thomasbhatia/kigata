import os

# Default settings example!
# To use this file set ENV like this:
# export SERVER_ENV="DEV" 
# or
# export SERVER_ENV="TEST" 
#
# To test the live example file, unset SERVER_ENV and set KIGATA_SETTINGS 

# For option details see:
# See http://flask.pocoo.org/docs/0.10/config/

# This helps to get errors into httpd logs
PROPAGATE_EXCEPTIONS = True


# Set the appropriate config in app/factory.py under app.config.from_object('app.settings.DevConfig')
class DevConfig(object):
    # server_env = os.getenv('SERVER_ENV')
    # Server Listening IP address or FQDN
    HOST = '0.0.0.0'
    # Serve Port
    PORT = 8080
    # Server name
    SERVER_NAME = '0.0.0.0:8080'
    # Debug True or False
    DEBUG = False
    # APP secret key
    SECRET_KEY = '?\xb3,\xb2\x8d\xa3"<\x1c\xb0@\x0f5\xab,w\xff\x7d$0\x13\x8b81'
    ## Mongodb Config
    MONGO_URI = 'mongodb://user:pas@ds012345.mlab.com:12345/dbname'


