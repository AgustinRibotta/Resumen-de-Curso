from django.contrib import admin
from django.urls import path
from .views import curso, lista_curso, profesores, estudiantes, entregables, cursos, inicio, cursoFormulario, busqueda_camada, buscar

urlpatterns = [
    path('curso/<nombre>/<camada>',curso),
    path('',inicio, name ="Inicio"),
    path('lista_curso/',lista_curso),
    path('cursos/',cursos, name="Cursos"), # El tercer atributo nos permite inhdicar en el html a donde nos vamos a dirifir
    path('profesores/',profesores, name="Profesores" ),
    path('estudiantes/',estudiantes, name="Estudiantes"),
    path('entregables/',entregables, name="Entregas"),
    path('cursoFormulario/',cursoFormulario, name="CursoFormulario"),  # Creamo la url para esa funcion.
    path('busquedaCamada/',busqueda_camada, name='BusquedaCamada'),
    path('buscar/',buscar, name='Buscar')
]

