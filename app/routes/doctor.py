from flask import Blueprint, render_template
from flask_login import login_required, current_user

bp = Blueprint('doctor', __name__)


@bp.route('/doctors')
@login_required
def doctor_index():
    # Assuming there's a way to identify doctors
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    return render_template('doctor/index.html', title='Doctor Dashboard')