import os
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False


def create_app(config_class='config.Config'):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # handles the email provider's SMTP server "gmail"
    app.config['MAIL_PORT'] = 587  # Typically 587 for TLS or 465 for SSL
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    app.config['MAIL_USERNAME'] = 'acleff73@gmail.com'
    app.config['MAIL_PASSWORD'] = '360Kid42984'
    app.config['MAIL_DEFAULT_SENDER'] = ('MedEase hospital', 'acleff73@gmail.com')

    db = SQLAlchemy(app)
    mail = Mail(app)
    ...
