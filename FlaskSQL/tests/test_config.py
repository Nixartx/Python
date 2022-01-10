"""Flask configuration."""
import os

basedir = os.path.abspath(os.path.dirname(__file__))

# Postgres port 5432


class Config:
    TESTING = True
    DEBUG = True
    FLASK_ENV = 'development'
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev'),
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin@localhost/PostgreDBtest'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
