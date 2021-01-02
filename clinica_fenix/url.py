from django.urls import path
from . import views

app_name = "clinica_fenix"

urlpatterns = [
    path("", views.inicio),
    path("login/", views.login, name = "login" ),
    path("pagina_privada/", views.private_page, name ="portal_privado" ),
    path("usuario_nuevo/", views.nuevo_usuario, name="nuevo_usuario" ),
    path("lista_usuarios/", views.usuarios_registrados, name="lista_usuario"),
    path("<id>/borrar/",views.eliminar_cliente, name="eliminar_cliente"),
    path("<id>/render/", views.render_cliente, name="render_cliente"),
]
