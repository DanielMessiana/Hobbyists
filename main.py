from flask import Flask
from flask import render_template
from flask import request
from flask import url_for

hobbyists = Flask(__name__)

@hobbyists.route("/")
def start():
	return render_template("start.html")

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
