import os 
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(basedir, '.env')


class Config(object):
    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL?ssl=require') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Form protection
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # Pagination
    POSTS_PER_PAGE = int(os.environ.get('POSTS_PER_PAGE'))

    # Email configuration
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = os.environ.get('ADMINS')

    # Heroku logs
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')

    # Auth0
    AUTHO_DOMAIN = os.environ.get('AUTHO_DOMAIN')
    AUTHO_CLIENT_ID = os.environ.get('AUTHO_CLIENT_ID')
    AUTHO_CLIENT_SECRET = os.environ.get('AUTHO_CLIENT_SECRET')
    AUTH0_CALLBACK_URL = os.environ.get('AUTH0_CALLBACK_URL')

    # Localhost testing
    START_NGROK = os.environ.get('START_NGROK')
