from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from config import Config
mail = Mail()

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'


def create_app(config_class='config.Config'):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    # Initialize extensions
    mail.init_app(app)

    # Register blueprints
    from app.email.route import bp as email_bp
    app.register_blueprint(email_bp)

    from app.routes import auth, patient, doctor, appointment, home_page
    
    app.register_blueprint(auth.bp)
    app.register_blueprint(patient.bp)
    app.register_blueprint(doctor.bp)
    app.register_blueprint(appointment.bp)
    if app.register_blueprint(home_page.bp):
        print("homepage imported")

    return app
