from django.shortcuts import render
from django.http import HttpResponse
from .models import Preferences
from .forms import QuestioneOne

def index(response):
	return HttpResponse("<h1>test</h1>")

def start(response):
	return render(response, "main/start.html", {})


def secret(response):
	return render(response, "main/secret.html", {})

def test(response):
	if response.method == "POST":
		form = QuestioneOne(response.POST)

	else:
		form = QuestioneOne()

	return render(response, "main/test.html", {"form":form})

def results(response):

	return render(response, "main/results.html", {})