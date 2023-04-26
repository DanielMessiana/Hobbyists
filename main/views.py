from django.shortcuts import render
from django.http import HttpResponse


def index(response):
	return HttpResponse("<h1>test</h1>")

def start(response):
	return render(response, "main/start.html", {})

def secret(response):
    if request.method == 'POST':
        question1 = request.POST.get('question1')
        question2 = request.POST.get('question2')
        question3 = request.POST.getlist('question3[]')
        # Process the survey data here
        return render(request, 'survey_confirmation.html')
    else:
        return render(request, 'survey.html')
    return render(response, "main/secret.html", {})

def survey(response):
	return render(response, 'main/survey.html')

def results(response):
	return render(response, "main/results.html", {})