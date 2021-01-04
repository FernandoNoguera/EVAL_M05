from django.shortcuts import render, redirect 
from django.conf import settings
from .forms import IngresoUsuario,NewUser
import json

def inicio(request):  
    return render(request, 'clinica_py/index.html')

def login(request):
    formulario = IngresoUsuario(request.POST or None)
    context = {'form':formulario}
    if formulario.is_valid():
        form_data = formulario.cleaned_data
        filename = "/clinica_py/static/clinica_py/data/usuario.json"
        with open(str(settings.BASE_DIR)+filename, 'r') as file:
            usuario=json.load(file)
        if (form_data['usuario'] == usuario['usuario']) and (form_data['clave'] == usuario['clave']):
            return redirect('clinica_fenix:portal_privado')               
        else:
            return redirect('clinica_fenix:login')               
    return render(request, 'clinica_py/registro.html',context)
















def private_page(request):
    listaedad = []
    listapellido = []
    filename= "/clinica_py/static/clinica_py/data/clientes.json"
    with open(str(settings.BASE_DIR)+filename, "r") as file:
        usuarios = json.load(file)
        diccionario = usuarios.get('usuario')
        for elemento in diccionario[-5:]:
            edad = elemento.get('edad')
            edad = int(edad)
            listaedad.append(edad)
        for elemento in diccionario[-5:]:

            apellido = elemento.get('apellido_paterno')
            apellido = apellido[5, len(apellido)-5]
            listapellido.append(apellido)

            
            print(listaedad,listapellido)
    context = {'edades' : listaedad, 'apellidos': listapellido}
    return render(request, 'clinica_py/PagePrivate.html', context)











def nuevo_usuario(request):
    formulario = NewUser(request.POST or None)
    context = {'form':formulario}
    if formulario.is_valid():
        form_data = formulario.cleaned_data
        filename= "/clinica_py/static/clinica_py/data/clientes.json"
        with open(str(settings.BASE_DIR)+filename, 'r') as file:
            usuario=json.load(file)
        form_data['id'] = usuario['ultimo_id_generado'] + 1
        usuario['ultimo_id_generado'] = form_data['id']
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

def eliminar_cliente(request, id):
    if request.method == "POST":
        filename= "/clinica_py/static/clinica_py/data/clientes.json"
        with open(str(settings.BASE_DIR)+filename, 'r') as file:
            clientes=json.load(file)
        for cliente in clientes['usuario']:
            if int(cliente['id']) == int(id):
                clientes['usuario'].remove(cliente)
                break
        with open(str(settings.BASE_DIR)+filename, 'w') as file:
            json.dump(clientes, file)
        return redirect('clinica_fenix:lista_usuario')
    context = {'id':id}
    return render(request, 'clinica_py/eliminar_cliente.html', context)

def render_cliente(request, id):
    filename= "/clinica_py/static/clinica_py/data/clientes.json"
    with open(str(settings.BASE_DIR)+filename, 'r') as file:
        clientes=json.load(file)
    for cliente in clientes['usuario']:
        if int(cliente['id']) == int(id):
            cliente_datos = cliente
    context = {'id':id, 'cliente': cliente_datos }
    return render(request, 'clinica_py/render_cliente.html', context)


