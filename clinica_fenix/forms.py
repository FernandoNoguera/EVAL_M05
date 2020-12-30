from django import forms


class IngresoUsuario(forms.Form):
    usuario = forms.CharField()
    #contraseña = forms.CharField()
    #contraseña2 = forms.PasswordInput()
 
