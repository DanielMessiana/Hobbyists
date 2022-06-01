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

		if form.is_valid():
			inside = form.cleaned_data['Inside']
			outside = form.cleaned_data['Outside']
			either = form.cleaned_data['Either']

			if inside:
				t = Preferences(text="inside")
				t.save()
			if outside:
				t = Preferences(text="outside")
				t.save()
			if either:
				t = Preferences(text="either")
				t.save()

	else:
		form = QuestioneOne()

	return render(response, "main/test.html", {"form":form})

def results(response):

	return render(response, "main/results.html", {})