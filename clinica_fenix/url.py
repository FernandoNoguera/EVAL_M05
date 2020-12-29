from django.urls import path
from . import views

#app_name = "app_ex"

urlpatterns = [
    path("inicio/", views.inicio),   
]