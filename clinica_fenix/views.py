from django.shortcuts import render, redirect 
from django.conf import settings
from .forms import IngresoUsuario
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
        usuario['usuario'].append(form_data)
        with open(str(settings.BASE_DIR)+filename, 'w') as file:
            json.dump(usuario, file)
        return redirect('clinica_fenix:portal_privado')
        

                
    return render(request, 'clinica_py/registro.html',context)

def private_page(request):
    return render(request, 'clinica_py/PagePrivate.html')

