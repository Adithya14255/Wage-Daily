from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql://admin:admin@localhost:5432/wagedaily')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "wagedailysecretkey2025"

db = SQLAlchemy(app)

# Database Models
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

class JobRequest(db.Model):
    __tablename__ = 'job_requests'
    id = db.Column(db.Integer, primary_key=True)
    employer_name = db.Column(db.String(100), nullable=False)
    job_type = db.Column(db.String(50), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    locality = db.Column(db.String(100), nullable=False)
    pincode = db.Column(db.String(10), nullable=False)
    contact = db.Column(db.String(20), nullable=False)
    workers_required = db.Column(db.Integer, nullable=False)
    wage = db.Column(db.Integer, nullable=False)

# Routes
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/home')
def home():
    job_requests = JobRequest.query.all()
    username = session.get('username', '')
    return render_template("home.html", result=job_requests, uname=username)

@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        
        user = User.query.filter_by(username=username, password=password).first()
        
        if user:
            session['user_id'] = user.id
            session['username'] = user.username
            return redirect(url_for('dashboard'))
        else:
            message = "Invalid Username/Password"
    
    return render_template("signup.html", message=message)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    message = ''
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        
        # Check if user already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            message = "Username already exists"
            return render_template('signup.html', message=message)
        
        # Create new user
        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        
        return redirect(url_for('login'))
    
    return render_template('signup.html', message=message)

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    job_requests = JobRequest.query.all()
    return render_template("dashboard.html", job_requests=job_requests, username=session['username'])
@app.route('/add_request', methods=['GET', 'POST'])
def add_request():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        employer_name = request.form["employer_name"]
        job_type = request.form["job_type"]
        district = request.form["district"]
        locality = request.form["locality"]
        pincode = request.form["pincode"]
        contact = request.form["contact"]
        workers_required = request.form["workers_required"]
        wage = request.form["wage"]
        
        new_request = JobRequest(
            employer_name=employer_name,
            job_type=job_type,
            district=district,
            locality=locality,
            pincode=pincode,
            contact=contact,
            workers_required=workers_required,
            wage=wage
        )
        
        db.session.add(new_request)
        db.session.commit()
        
        return redirect(url_for('dashboard'))
  
    return render_template("add_request.html", username=session['username'])

@app.route('/request_details/<int:request_id>')
def request_details(request_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    job_request = JobRequest.query.get_or_404(request_id)
    return render_template("request_details.html", job_request=job_request, username=session['username'])

@app.route('/confirm_booking/<int:request_id>')
def confirm_booking(request_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    job_request = JobRequest.query.get_or_404(request_id)
    
    # Delete the job request after booking
    db.session.delete(job_request)
    db.session.commit()
    
    return render_template("booking_confirmed.html", username=session['username'])

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

@app.route('/about')
def about():
    if 'username' in session:
        return render_template("about.html", username=session['username'])
    return render_template("about.html")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
    app.run(debug=True, port=5001, host='0.0.0.0')