from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Curso, Profesor
from .forms import CursoFormulario, ProfesorFormulario
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

    lista = Curso.objects.all()

    return render(request,"curso.html",{"lista_curso":lista})

def profesores(request):

    return render(request,"profesores.html")

def estudiantes(request):

    return render(request,"estudiantes.html")

def entregables(request):

    return render(request,"entregables.html")
    
def cursoFormulario(request):  # Creamos la funciojn formularios.

    if request.method == "POST" :
        
        mi_formulario = CursoFormulario(request.POST) # Agregamos los formularios de Django.

        if mi_formulario.is_valid(): # Validacion del forulario.

            data = mi_formulario.cleaned_data
            curso = Curso(nombre=data['nombre'], camada=data['camada']) # Cargamos los datos del formulario
            curso.save()

        return redirect('Cursos') 
        
    else:
        
        mi_formulario = CursoFormulario()
    return render (request,"cursoFormulario.html",{"mi_formulario": mi_formulario})

def busqueda_camada (reques): # creamos la busqueda de cursos.

    return render(reques,'busqueda_camada.html')

def buscar (reques): # Realizamos la busqueda.

    camada_buscada = reques.GET["camada"]

    curso = Curso.objects.get(camada = camada_buscada)

    return render (reques, 'resultadoBusqeueda.html', {'curso':curso,'camada':camada_buscada})

# CRD

def lista_profesores(request):

    profesores = Profesor.objects.all() # Metodo para llamar a los archivos de la base de datos 'objects'.

    return render(request,'listaProfesores.html', {'profesores':profesores})

def crea_profesor(request):
        
    if request.method == "POST" :
        
        miFormulario = ProfesorFormulario(request.POST) # Agregamos los formularios de Django.

        if miFormulario.is_valid(): # Validacion del forulario.

            data = miFormulario.cleaned_data
            profesor = Profesor(nombre=data['nombre'], apellido=data['apellido'],email=data['email'], profesion=data['profesion']) # Cargamos los datos del formulario
            profesor.save()

            return redirect (inicio)
        
    else:
        
            miformulario = ProfesorFormulario()
            return render (request,"profesorFormulario.html",{"miformulario": miformulario})
    
def eliminarProfesor(request, id): # Eliminar un dato de la lsita
        
    if request.method == "POST" :
            
        profesor =Profesor.objects.get(id=id)
        profesor.delete()

        profesores = Profesor.objects.all() # Metodo para llamar a los archivos de la base de datos 'objects'.

        return render(request,'listaProfesores.html', {'profesores':profesores})



