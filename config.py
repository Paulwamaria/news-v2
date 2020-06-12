import os

class Config:
    '''
    The parent configuration class
    '''
    SECRECT_KEY=os.environ.get('SECRET_KEY')
    

class ProdConfig(Config):
    '''
    Child configuration class that holds the production configurations and also inherits from class Config
    '''
    pass

class DevConfig(Config):
    '''
    Child configuration class that holds development configarations and also inherits from the parent class Config.
    '''
    DEBUG = True

config_options = {
    'production':ProdConfig,
    'development':DevConfig
}