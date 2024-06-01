from flask import Blueprint, render_template
from flask_login import login_required, current_user

bp = Blueprint('home_page', __name__)

@app.route('/home_page')
@login_required
def landing():
    """Handles the landing page"""
    return render_template('home_page.html', title='Home',
                           headings=headings, MedEase=MedEase)