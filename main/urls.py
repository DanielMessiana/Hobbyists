from django.urls import path

from . import views


urlpatterns=[
path("temp", views.index, name="index"),
path("", views.start, name="start"),
path("secret", views.secret, name="secret"),
path("test", views.test, name="test"),
path("results", views.results, name="results")
]