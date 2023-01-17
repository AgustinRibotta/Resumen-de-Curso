from django.http import HttpResponse
from django.shortcuts import render
from .models import Curso
# Create your views here.

# De esta manera igresamos datos en nuestra base de datos.

def curso(request,nombre,camada):

    curso = Curso(nombre=nombre, camada=camada)
    curso.save()

    return HttpResponse(f""" 
    <p> Curso: {curso.nombre} - Camada: {curso.camada} agregado ! </p> 
    """)


# Sacar informacion de la base de datos.
# Metodo render.

def lista_curso(request):

    lista = Curso.objects.all()

    return render(request,"lista_curso.html",{"lista_curso":lista})


def inicio(request):

    return render(request,"inicio.html")

def cursos(request):

    return render(request,"curso.html")

def profesores(request):

    return render(request,"profesores.html")

def estudiantes(request):

    return render(request,"estudiantes.html")

def entregables(request):

    return render(request,"entregables.html")
    