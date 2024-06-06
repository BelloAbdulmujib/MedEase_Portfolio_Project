from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from datetime import datetime, timedelta

app = Flask(_name_)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hospital.db'
app.config['MAIL_SERVER'] = 'smtp.yourmailserver.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@example.com'
app.config['MAIL_PASSWORD'] = 'your_password'

db = SQLAlchemy(app)
mail = Mail(app)

# Database models
class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'), nullable=False)
    patient_name = db.Column(db.String(100), nullable=False)
    patient_email = db.Column(db.String(100), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)

# Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/book')
def book():
    doctors = Doctor.query.all()
    return render_template('book.html', doctors=doctors)

@app.route('/book/<int:doctor_id>', methods=['GET', 'POST'])
def book_doctor(doctor_id):
    doctor = Doctor.query.get_or_404(doctor_id)
    if request.method == 'POST':
        patient_name = request.form['patient_name']
        patient_email = request.form['patient_email']
        start_time = datetime.strptime(request.form['start_time'], '%Y-%m-%d %H:%M:%S')
        end_time = start_time + timedelta(hours=3)
        
        # Check for existing bookings
        existing_booking = Booking.query.filter(
            Booking.doctor_id == doctor_id,
            Booking.start_time < end_time,
            Booking.end_time > start_time
        ).first()

if existing_booking:
            flash(f'Doctor is booked from {existing_booking.start_time} to {existing_booking.end_time}.')
            return redirect(url_for('book_doctor', doctor_id=doctor_id))
        
        # Create new booking
        new_booking = Booking(
            doctor_id=doctor_id,
            patient_name=patient_name,
            patient_email=patient_email,
            start_time=start_time,
            end_time=end_time
        )
        db.session.add(new_booking)
        db.session.commit()
        
        # Send confirmation email
        msg = Message('Booking Confirmation', sender='your_email@example.com', recipients=[patient_email])
        msg.body = f'Your booking with Dr. {doctor.name} is confirmed from {start_time} to {end_time}.'
        mail.send(msg)
        
        flash('Booking successful!')
        return redirect(url_for('home'))
    
    return render_template('book_doctor.html', doctor=doctor)

if _name_ == '_main_':
    app.run(debug=True)