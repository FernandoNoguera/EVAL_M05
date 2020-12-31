from django import forms


class IngresoUsuario(forms.Form):
    usuario = forms.CharField()
    clave = forms.CharField(widget=forms.PasswordInput)

class new_user(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    edad = forms.CharField(widget=forms.NumberInput)
    rut = forms.CharField()
 
 
