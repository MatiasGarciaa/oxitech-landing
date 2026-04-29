from django.urls import path

from . import views

app_name = "oxitech"

urlpatterns = [
    path("", views.landing, name="landing"),
]
