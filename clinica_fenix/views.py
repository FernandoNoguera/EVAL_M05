from django.shortcuts import render, redirect 
from django.conf import settings
from .forms import IngresoUsuario,new_user
import json

def inicio(request):  
    return render(request, 'clinica_py/index.html')

def login(request):
    formulario = IngresoUsuario(request.POST or None)
    context = {'form':formulario}
    if formulario.is_valid():
        form_data = formulario.cleaned_data
        filename= "/clinica_py/static/clinica_py/data/usuario.json"
        with open(str(settings.BASE_DIR)+filename, 'r') as file:
            usuario=json.load(file)
        if (form_data['usuario'] == usuario['usuario']) and (form_data['clave'] == usuario['clave']):
            return redirect('clinica_fenix:portal_privado')               
        else:
#            print("No tiene acceso")
            return redirect('clinica_fenix:login')               
#        usuario['usuario'].append(form_data)
#        with open(str(settings.BASE_DIR)+filename, 'w') as file:
#            json.dump(usuario, file)
    return render(request, 'clinica_py/registro.html',context)

def private_page(request):
    return render(request, 'clinica_py/PagePrivate.html')

def nuevo_usuario(request):
    formulario = new_user(request.POST or None)
    context = {'form':formulario}
    if formulario.is_valid():
        form_data = formulario.cleaned_data
        filename= "/clinica_py/static/clinica_py/data/clientes.json"
        with open(str(settings.BASE_DIR)+filename, 'r') as file:
            usuario=json.load(file)
        usuario['usuario'].append(form_data)
        with open(str(settings.BASE_DIR)+filename, 'w') as file:
            json.dump(usuario, file)
        return redirect('clinica_fenix:lista_usuario')               
    return render(request, 'clinica_py/new_user.html', context)

def usuarios_registrados(request):
    filename= "/clinica_py/static/clinica_py/data/clientes.json"
    with open(str(settings.BASE_DIR)+filename, 'r') as file:
        clientes=json.load(file)
    return render(request, 'clinica_py/lista_usuario.html', context=clientes)
    

