from django.shortcuts import render
from django.conf import settings

def inicio(request):
    relleno = {}
    return render (request, 'clinica_py/index.html', context = relleno )