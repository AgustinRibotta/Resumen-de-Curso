from django.contrib import admin
from django.urls import path
from .views import curso, lista_curso, profesores, estudiantes, entregables, cursos, inicio

urlpatterns = [
    path('curso/<nombre>/<camada>',curso),
    path('',inicio, name ="Inicio"),
    path('lista_curso/',lista_curso),
    path('cursos/',cursos, name="Cursos"), # El tercer atributo nos permite inhdicar en el html a donde nos vamos a dirifir
    path('profesores/',profesores, name="Profesores" ),
    path('estudiantes/',estudiantes, name="Estudiantes"),
    path('entregables/',entregables, name="Entregas"),    
]

