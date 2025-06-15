import os, requests, json
from flask import Flask, render_template, request, url_for, redirect, flash, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

hobbyists = Flask(__name__)
hobbyists.secret_key = '046cfd55fa729b4ebc206d2f47387019f1ba8807c820943bb8ea26d6596f807e'
hobbyists.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
hobbyists.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(hobbyists)
login_manager = LoginManager(hobbyists)
login_manager.login_view = 'login'

OLLAMA_URL = "http://localhost:11434/api/generate"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Start page for the website
@hobbyists.route("/")
def home():
    return render_template("index.html")

@hobbyists.route('/api/hobbies')
def get_hobbies():
    with open('api/hobbies.json') as f:
        hobbies = json.load(f)
    return jsonify(hobbies)

# Sign up page for the website
@hobbyists.route('/join', methods=['GET', 'POST'])
def join():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("Username already exists", "danger")
            return redirect(url_for('join'))

        existing_email = User.query.filter_by(email=email).first()
        if existing_email:
            flash("Email already exists", "danger")
            return redirect(url_for('join'))

        hashed_password = generate_password_hash(password, method="pbkdf2:sha256", salt_length=8)
        new_user = User(username=username, password=hashed_password, email=email)
        db.session.add(new_user)
        db.session.commit()

        flash("Account created successfully", "success")
        return redirect(url_for('login'))
    return render_template("join.html")

# Login page for the website
@hobbyists.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            flash("Login successful", "success")
            return redirect(url_for('home'))
        else:
            flash("Invalid username or password", "danger")

    return render_template("login.html")

# Account page for the website
@hobbyists.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    if request.method == 'POST':
        if request.form.get('delete'):
            db.session.delete(current_user)
            db.session.commit()
            flash("Account deleted", "success")
            return redirect(url_for('home'))
        elif request.form.get('logout'):
            logout_user()
            flash("Logout successful", "success")
            return redirect(url_for('home'))
    else:
        return render_template("account.html")

# Survey page with LLM
@hobbyists.route("/survey", methods=['GET', 'POST'])
def survey():
    return render_template("survey.html")

@hobbyists.route("/generate-intro")
def generate_intro():
    payload = {
        "model": "mistral",
        "prompt": "You are a friendly assistant helping a user find new hobbies by giving them a short survey.",
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    if response.status_code == 200:
        data = response.json()
        return jsonify({"response": data.get("response", "")})
    else:
        return jsonify({"error": "Failed to connect to Ollama"}), 500



with hobbyists.app_context():
    db.create_all()

if __name__ == '__main__':
    hobbyists.run(host="0.0.0.0", port=5000)
