from django import forms


class IngresoUsuario(forms.Form):
    usuario = forms.CharField()
    clave = forms.CharField(widget=forms.PasswordInput)

class NewUser(forms.Form):
    primer_nombre = forms.CharField()
    segundo_nombre = forms.CharField()
    apellido_paterno = forms.CharField()
    apellido_materno = forms.CharField()
    edad = forms.CharField(widget=forms.NumberInput)
    rut = forms.CharField()
    nacionalidad = forms.CharField()
    teléfono = forms.CharField(widget=forms.NumberInput)
    dirección = forms.CharField()
  