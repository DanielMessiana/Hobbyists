import os
from flask import Flask, render_template, request, url_for, redirect, flash, session
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

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Start page for the website
@hobbyists.route("/")
def home():
    return render_template("index.html")

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

# Survey page for our hobby ai
@hobbyists.route("/survey", methods=['POST'])
def survey():
    if request.method == 'POST':
        question1 = request.POST.get('question1')
        question2 = request.POST.get('question2')
        question3 = request.POST.get('question3')
        question4 = request.POST.get('question4')
        question5 = request.POST.get('question5')
        question6 = request.POST.get('question6')
        question7 = request.POST.get('question7')
        question8 = request.POST.get('question8')
        question9 = request.POST.get('question9')
        question10 = request.POST.get('question10')
        question11 = request.POST.get('question11')

        answers = [question1, question2, question3, question4, question5, question6, question7, question8, question9, question10, question11]
        return render_template("survey_results.html")
    else:

        return render_template("survey.html")

with hobbyists.app_context():
    db.create_all()

if __name__ == '__main__':
    hobbyists.run(debug=True)
