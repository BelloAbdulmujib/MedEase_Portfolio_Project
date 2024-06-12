from flask import Blueprint

bp = Blueprint('email', __name__)

@bp.route ('/send_email')
def send_email():
    return "Email sent"