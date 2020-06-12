import os

class Config:
    '''
    The parent configuration class
    '''
    SECRECT_KEY=os.environ.get('SECRET_KEY')
    API_KEY=os.environ.get('API_KEY')

    NEWS_SOURCES_BASE_URL='https://newsapi.org/v2/sources?apikey={}'
    ARTICLES_BASE_URL='https://newsapi.org/v2/everything?q={}&apikey={}'
    TOP_HEADLINE_BASE_URL='https://newsapi.org/v2/top-headline?category={}&apikey={}'



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