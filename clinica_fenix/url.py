from django.urls import path
from . import views

app_name = "clinica_fenix"

urlpatterns = [
    path("", views.inicio),
    path("login/", views.login, name = "login" ),
    path("pagina_privada/", views.private_page, name ="portal_privado" ),
]