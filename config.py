import os


database_url = os.getenv('DATABASE_URL', 'sqlite:///mechanic.db')

class DevelopmentConfig:    
    SQLALCHEMY_DATABASE_URI = database_url
    DEBUG = True
    CACHE_TYPE = 'SimpleCache'

class TestingConfig:
    pass

class ProductionConfig:
    pass