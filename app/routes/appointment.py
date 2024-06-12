from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.models import Appointment
from app.forms import AppointmentForm
from datetime import timedelta
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message

mail = Mail()
bp = Blueprint('appointment', __name__)

@bp.route('/appointments')
@login_required
def index():
    """Handles the appointment route"""
    appointments = Appointment.query.filter_by(patient_id=current_user.id).all()
    return render_template('appointment/index.html', appointments=appointments)

from flask_login import current_user

@bp.route('/appointments/book', methods=['GET', 'POST'])
@login_required
def book():
    """Handles the booking route"""
    form = AppointmentForm()
    if form.validate_on_submit():
        doctor_id = form.doctor_id.data
        date = form.date.data
        start_time = form.start_time.data
        end_time = form.end_time.data

        # Check for overlapping appointments
        existing_appointments = Appointment.query.filter_by(doctor_id=doctor_id, date=date).all()
        for appointment in existing_appointments:
            if (start_time < appointment.start_time and end_time > appointment.start_time):
                flash('Booking cannot take place because another user has booked the same time slot.')
                return redirect(url_for('book'))

        # If no overlap, create the appointment
        new_appointment = Appointment(
            doctor_id=doctor_id,
            patient_id=current_user.id,  # Assign the current user's ID
            date=date,
            start_time=start_time,
            end_time=end_time,
            notes=form.notes.data
        )
        db.session.add(new_appointment)
        db.session.commit()

        # Send confirmation email
        user_email = request.form.get('email')  # Assuming you have an email field in your form
        send_confirmation_email(user_email, new_appointment)

        flash('Appointment booked successfully!')
        return redirect(url_for('index'))
    else:
        print(form.errors)  # Print form errors for debugging

    return render_template('appointment/book.html', form=form)


def send_confirmation_email(to_email, appointment):
    """sends confirmation email"""
    msg = Message('Appointment Confirmation',
                  recipients=[to_email])
    msg.body = f'''Dear User,

Your appointment has been successfully booked.

Doctor ID: {appointment.doctor_id}
Date: {appointment.date.strftime('%Y-%m-%d')}
Start Time: {appointment.start_time.strftime('%H:%M')}
End Time: {appointment.end_time.strftime('%H:%M')}
Notes: {appointment.notes}

Thank you,
MedEase Healthcare
'''
    mail.send(msg)