"""Flask configuration."""
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    TESTING = True
    DEBUG = True
    FLASK_ENV = 'development'
    SECRET_KEY=os.environ.get('SECRET_KEY', 'dev'),
    DATABASE=os.path.join(basedir, 'db\monaco.db'),


