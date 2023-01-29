# Archivo de formularios.

from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm  # Formulario para login
from django.contrib.auth.models import User

# Creamos un formulario atravez de django.

class CursoFormulario (forms.Form):

    nombre = forms.CharField(max_length=50) # Creamo un objeto del tipo charfild.
    camada = forms.IntegerField()

# Prodesor formulario.
 
class ProfesorFormulario (forms.Form):

    nombre = forms.CharField(max_length=50) # Creamo un objeto del tipo charfild.
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=50)

# Editar usuario
# Generamos las variables password 1  y 2 Para luego ahcer la verificacion de igualdad.
class UserEditForm(UserChangeForm):

    password = forms.CharField(
    help_text="",
    widget=forms.HiddenInput(), required=False
    )

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ['email','first_name','last_name','password1','password1']

    #Verificacion

    def clean_password2(self):
        
        password2 = self.cleaned_data["password2"]
        password1 = self.cleaned_data["password1"]

        if password2 != password1:
            raise forms.ValidationError("Las contraseñas no coinciden!")
        
        return password2
    

# Registro personalisado

class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('__all__')



    



