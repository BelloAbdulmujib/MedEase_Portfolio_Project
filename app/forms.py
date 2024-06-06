from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, TimeField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import User
from wtforms.fields import DateField, EmailField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    """Handles the login form detail"""
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    """Handles the registration form detail"""
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        """user validation"""
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        """email validation"""
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


class AppointmentForm(FlaskForm):
    """Handles the Appointment form detail"""
    doctor_id = StringField('Doctor ID', validators=[DataRequired()])
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    start_time = TimeField('Start Time', validators=[DataRequired()])
    end_time = StringField('End Time', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    notes = StringField('Notes')
    submit = SubmitField('Book')
