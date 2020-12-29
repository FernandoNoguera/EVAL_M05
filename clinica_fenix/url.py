from django.urls import path
from . import views

app_name = "clinica_fenix"

urlpatterns = [
    path("", views.inicio),
    path("login/", views.login)
       
]