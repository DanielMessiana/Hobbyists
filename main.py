from flask import Flask
from flask import render_template
from flask import url_for

hobbyists = Flask(__name__)

@hobbyists.route("/")
def start():
	return render_template("start.html")

@hobbyists.route("/survey")
def survey():
	return render_template("survey.html")
