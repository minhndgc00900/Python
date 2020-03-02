class StandardConfig(object):
    MESSAGE="Hello World!"
    pass

class DevConfig(StandardConfig):
    DEBUG = True
    ENV = "development"

class ProdConfig(StandardConfig):
    DEBUG = False
    ENV = "production"