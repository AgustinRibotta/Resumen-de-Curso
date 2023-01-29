from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (curso, 
                    lista_curso, 
                    profesores, 
                    estudiantes, 
                    entregables, 
                    cursos, inicio, 
                    cursoFormulario, 
                    busqueda_camada, buscar,lista_profesores,crea_profesor,eliminarProfesor, edita_profesor, CursoList, CursoDetail, CursoCreate, CursoUpdate, 
                    CursoDelete, loginView,register,
                    editar_perfil)


urlpatterns = [
    path('curso/<nombre>/<camada>',curso),
    path('',inicio, name ="Inicio"),
    path('lista_curso/',lista_curso),
    path('cursos/',cursos, name="Cursos"), # El tercer atributo nos permite inhdicar en el html a donde nos vamos a dirifir
    path('profesores/',profesores, name="Profesores" ),
    path('estudiantes/',estudiantes, name="Estudiantes"),
    path('entregables/',entregables, name="Entregas"),
    path('cursoFormulario/',cursoFormulario, name="CursoFormulario"),  # Creamo la url para esa funcion.
    path('busquedaCamada/',busqueda_camada, name='BusquedaCamada'), # Creamos url para busqueda de cursos.
    path('buscar/',buscar, name='Buscar'), # Muestra el curso.
    path('listaProfesores/', lista_profesores, name = 'ListaProfesores'), # Lee los archivos de la base de datos.
    path('crea_profesor/', crea_profesor, name = 'CreaProfesor'),
    path('elimina_profesor/<int:id>', eliminarProfesor, name = 'EliminaProfesor'),
    path('editar_profesor/<int:id>', edita_profesor, name = 'EditarProfesor'),
    path('listaCurso/', CursoList.as_view(), name = 'ListaCursos'),
    path('detalleCurso/<pk>', CursoDetail.as_view(), name = 'DetallCurso'),
    path('creaCurso/', CursoCreate.as_view(), name = 'CreaCurso'),
    path('actualizarCurso/<pk>', CursoUpdate.as_view(), name = 'ActualizarCursos'),
    path('eliminarCurso/<pk>', CursoDelete.as_view(), name = 'EliminaCurso'),  
    path('login/',loginView, name = 'Login'),
    path('registre/',register, name = 'Registrar'),            
    path('logout/',LogoutView.as_view(template_name='logout.html'), name = 'Logout'),  
    path('editar-perfil/',editar_perfil, name = 'EditarPerfil'),
]   

