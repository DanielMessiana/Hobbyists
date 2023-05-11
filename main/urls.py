from django.urls import path

from . import views


urlpatterns=[
path("temp", views.index, name="index"),
path("", views.start, name="start"),
path("survey", views.survey_view, name="survey_view"),
path("results", views.results, name="results")
]