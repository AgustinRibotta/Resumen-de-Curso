# Archivo de formularios.

from django import forms

# Creamos un formulario atravez de django.

class CursoFormulario (forms.Form):

    nombre = forms.CharField(max_length=50) # Creamo un objeto del tipo charfild.
    camada = forms.IntegerField()