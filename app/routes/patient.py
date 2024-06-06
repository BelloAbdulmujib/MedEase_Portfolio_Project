from flask import Blueprint, render_template
from flask_login import login_required, current_user

bp = Blueprint('patient', __name__)

@bp.route('/patients')
@login_required
def patient_index():
    """Patients Authentication"""
    # Assuming there's a way to identify patients
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    return render_template('patient/index.html', title='Patient Dashboard')
