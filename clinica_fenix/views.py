from django.shortcuts import render
from django.conf import settings

def inicio(request):  
    return render(request, 'clinica_py/index.html')

def login(request):
    return render(request, 'clinica_py/registro.html')

def private_page(request):
    return render(request, 'clinica_py/PagePrivate.html')
