from flask import Flask
from flask_mail import Mail, Message

@app.route('/send_email')
def send_email():
    """sent's email after successful booking"""
    msg = Message('Hello from Flask', recipients=['recipient@example.com'])
    msg.body = 'This is a test email sent from a Flask application!'
    mail.send(msg)
    return 'Email sent!