from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from app import db
from app.models import Appointment

bp = Blueprint('appointment', __name__)


@bp.route('/appointments', methods=['GET', 'POST'])
@login_required
def appointment_index():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    appointments = Appointment.query.filter_by(patient_id=current_user.id).all()
    return render_template('appointment/index.html', title='Appointments', appointments=appointments)
