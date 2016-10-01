class BaseConfig(object):
    PROJECT = 'genecardapi'

    DEBUG = False


class DefaultConfig(BaseConfig):
    DEBUG = True
    MONGO_DB_USERNAME = 'admin'
    MONGO_DB_PASSWORD = 'password'
    MONGO_DB_HOST = '127.0.0.1'
    MONGO_DB_URL = 'mongodb://%s:%s@%s' % (MONGO_DB_USERNAME, MONGO_DB_PASSWORD, MONGO_DB_HOST)
