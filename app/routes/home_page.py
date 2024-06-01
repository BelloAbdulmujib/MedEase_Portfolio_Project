from flask import Blueprint, render_template
from flask_login import login_required, current_user

bp = Blueprint('home_page', __name__)


@bp.route('/home_page')
@login_required
def index():
    """Handles the home page"""
    return render_template('home_page.html', title='Home',
                           headings='MedEase', MedEase='MedEase')

@bp.route('/')
def landing():
    """Landing page"""
    return render_template('landing.html', title='Landing')