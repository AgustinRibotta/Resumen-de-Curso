# Archivo de formularios.

from django import forms

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