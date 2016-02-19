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
    DEBUG = True

    # APP secret key
    SECRET_KEY = '?\xb3,\xb1\x8d\xa3"<\x9c\xb0@\x0f5\xab,w\xff\x8d$0\x13\x8b81'

    ## Mongodb Config
    # DB 1:
    # MONGO_PREFIX = 'MONGO_TEST1'
    # Mongo Server
    MONGO_SERVER = 'ds039301.mongolab.com'
    # Mongo Port
    MONGO_PORT = '39301'
    # Mongo Username
    MONGO_USERNAME = 'drone2'
    # Mongo Password
    MONGO_PASSWORD = 'icarus'
    # Mongo DB name
    MONGO_DBNAME = 'etgeonet'


    ## Mongodb Config
    # DB 2:
    MONGO_PREFIX2 = 'MONGO_TEST2'
    # Mongo Host
    MONGO_SERVER2 = 'ds012345.mongolab.com'
    # Mongo Port
    MONGO_PORT2 = 12345
    # Mongo Username
    MONGO_USERNAME2 = 'user2'
    # Mongo Password
    MONGO_PASSWORD2 = 'passwd2'
    # Mongo DB name
    MONGO_DBNAME2 = 'db_test2'


class TestConfig(object):
    # Server Listening IP address or FQDN
    HOST = '0.0.0.0'
    # Serve Port
    PORT = 8081
    # Server name
    SERVER_NAME = '127.0.0.1:8081'
    # Debug True or False
    DEBUG = True

    # APP secret key
    SECRET_KEY = '?\xb3,\xb1\x9a\xa3"<\x9c\xb0@\x0f5\xab,w\xff\x8d$0\x13\x8b81'

    ## Mongodb Config
    # DB 1:
    # MONGO_PREFIX = 'MONGO_TEST1'
    # Mongo Server
    MONGO_SERVER = 'ds039301.mongolab.com'
    # Mongo Port
    MONGO_PORT = '39301'
    # Mongo Username
    MONGO_USERNAME = 'drone2'
    # Mongo Password
    MONGO_PASSWORD = 'icarus'
    # Mongo DB name
    MONGO_DBNAME = 'etgeonet'


    ## Mongodb Config
    # DB 2:
    MONGO_PREFIX2 = 'MONGO_TEST2'
    # Mongo Host
    MONGO_SERVER2 = 'ds012345.mongolab.com'
    # Mongo Port
    MONGO_PORT2 = 12345
    # Mongo Username
    MONGO_USERNAME2 = 'user2'
    # Mongo Password
    MONGO_PASSWORD2 = 'passwd2'
    # Mongo DB name
    MONGO_DBNAME2 = 'db_test2'


class LiveConfig(object):
    # Server Listening IP address or FQDN
    HOST = '0.0.0.0'
    # Serve Port
    PORT = 8081
    # Server name
    SERVER_NAME = '127.0.0.1:8081'
    # Debug True or False
    DEBUG = True

    # APP secret key
    SECRET_KEY = '?\xb3,\xb1\x9a\xa3"<\x9c\xb0@\x0f5\xab,w\xff\x8d$0\x13\x8b81'

    ## Mongodb Config
    # DB 1:
    # MONGO_PREFIX = 'MONGO_TEST1'
    # Mongo Server
    MONGO_SERVER = 'ds039301.mongolab.com'
    # Mongo Port
    MONGO_PORT = '39301'
    # Mongo Username
    MONGO_USERNAME = 'drone2'
    # Mongo Password
    MONGO_PASSWORD = 'icarus'
    # Mongo DB name
    MONGO_DBNAME = 'etgeonet'


    ## Mongodb Config
    # DB 2:
    MONGO_PREFIX2 = 'MONGO_TEST2'
    # Mongo Host
    MONGO_SERVER2 = 'ds012345.mongolab.com'
    # Mongo Port
    MONGO_PORT2 = 12345
    # Mongo Username
    MONGO_USERNAME2 = 'user2'
    # Mongo Password
    MONGO_PASSWORD2 = 'passwd2'
    # Mongo DB name
    MONGO_DBNAME2 = 'db_test2'

