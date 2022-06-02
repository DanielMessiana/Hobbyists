from django.shortcuts import render
from django.http import HttpResponse
from .models import Preference

def index(response):
	return HttpResponse("<h1>test</h1>")

def start(response):
	return render(response, "main/start.html", {})


def secret(response):
	return render(response, "main/secret.html", {})

def test(response):

	return render(response, "main/test.html", {})

def results(response):

	return render(response, "main/results.html", {})