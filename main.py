from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import session
from flask_login import LoginManager
import sqlite3

hobbyists = Flask(__name__)
hobbyists.secret_key = '046cfd55fa729b4ebc206d2f47387019f1ba8807c820943bb8ea26d6596f807e'

login_manager = LoginManager()
login_manager.init_app(hobbyists)

# User database for storing user information
connection = sqlite3.connect('databases/users.db')
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT,
    password TEXT,
    email TEXT,
    hobbies TEXT
)
""")
connection.commit()
connection.close()

@login_manager.user_loader
def load_user(user_id):
    connection = sqlite3.connect('databases/users.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()

    return user

# Start page for the website
@hobbyists.route("/")
def index():
    if request.method == 'POST':
        hobby = request.form.get('hobbies')

        print(hobby)

    return render_template("index.html")

# Sign up page for the website
@hobbyists.route('/join')
def join():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')

        connection = sqlite3.connect('databases/users.db')
        cursor = connection.cursor()

        cursor.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)", (username, password, email))
        connection.commit()
        connection.close()

        return render_template("join.html")
    else:
        return render_template("join.html")

# Login page for the website
@hobbyists.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        connection = sqlite3.connect('databases/users.db')
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()

        if user:
            login_user(user)

            next = request.args.get('next')

            if not is_safe_url(next):
                return abort(400)

            return render_template("login.html")
        return render_template("login.html")

    return render_template("login.html")

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

