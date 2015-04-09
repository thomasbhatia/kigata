import os
class Config(object):
    server_env = os.getenv('SERVER_ENV')

        if server_env == 'DEV':
            # Server Listening IP address or FQDN
            HOST = '0.0.0.0'
            # Serve Port
            PORT = 8081
            # Server name
            SERVER_NAME = '127.0.0.1:8080'
            # Debug True or False
            DEBUG = True

            # APP secret key
            SECRET_KEY = '?\xb3,\xb1\x8d\xa3"<\x9c\xb0@\x0f5\xab,w\xff\x8d$0\x13\x8b81'

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

        elif server_env == 'DEV':
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

