# Live settings example!
# To use this file set ENV like this:
# export KIGATA_SETTINGS="/opt/Kigata/misc/config.py"

# For option details see:
# See http://flask.pocoo.org/docs/0.10/config/ 

# This helps to get errors into httpd logs
PROPAGATE_EXCEPTIONS = False

# Server Listening IP address or FQDN
HOST = '0.0.0.0'
# Serve Port
PORT = 8082
# Debug True or False
DEBUG = False
# Server name
SERVER_NAME = '127.0.0.1:8082'
# Full name
FULL_SERVER_NAME = 'Kigata Live server'
# import config

# APP secret key
SECRET_KEY = '?\xbf,\xb4\x8d\xa3"<\x9c\xb0@\x0f5\xab,w\xee\x8d$0\x13\x8b83'

## Mongodb Config 
# DB 1:
MONGO_PREFIX = 'MONGO_TEST1'
# Mongo Host
MONGO_TEST1_HOST = 'ds054321.mongolab.com'
# Mongo Port
MONGO_TEST1_PORT = 54321
# Mongo Username
MONGO_TEST1_USERNAME = 'user1'
# Mongo Password
MONGO_TEST1_PASSWORD = 'passwd1'
# Mongo DB name
MONGO_ETAAA_DBNAME = 'db_test1'

## Mongodb Config 
# DB 2:
MONGO_PREFIX = 'MONGO_TEST2'
# Mongo Host
MONGO_TEST2_HOST = 'ds012345.mongolab.com'
# Mongo Port
MONGO_TEST2_PORT = 12345
# Mongo Username
MONGO_TEST2_USERNAME = 'user2'
# Mongo Password
MONGO_TEST2_PASSWORD = 'passwd2'
# Mongo DB name
MONGO_TEST2_DBNAME = 'db_test2'



