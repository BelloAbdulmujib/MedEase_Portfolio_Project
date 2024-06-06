from datetime import datetime
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta

class User(UserMixin, db.Model):
    """Handles the user database"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'


class Patient(db.Model):
    """Handles the patient database"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(64))
    date_of_birth = db.Column(db.Date)
    # other patient-related fields

    def __repr__(self):
        return f'<Patient {self.name}>'


class Doctor(db.Model):
    """Handles the doctor's database"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(64))
    specialty = db.Column(db.String(64))
    # other doctor-related fields

    def __repr__(self):
        return f'<Doctor {self.name}, {self.specialty}>'


class Appointment(db.Model):
    """Handles Appointment database"""
    id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)
    notes = db.Column(db.String(200), nullable=True)
    
    # other appointment-related fields

    def __repr__(self):
        return f'<Appointment {self.id} with Doctor {self.doctor_id}>'


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
