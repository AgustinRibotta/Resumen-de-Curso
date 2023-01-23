from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Curso, Profesor
from .forms import CursoFormulario, ProfesorFormulario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView

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



# CRUD  Creat - Read - Upgrade - Delet

# Read - Recuperamos toda la lista de profesores.

def lista_profesores(request):

    profesores = Profesor.objects.all() # Metodo para llamar a los archivos de la base de datos 'objects'.

    return render(request,'listaProfesores.html', {'profesores':profesores}) #  Creamos el Html qqeuc ontiene el listado.

# Creat - Creamos un profesor.
# Request tipos POST: para actualizar un recurso del servidor.
# Rquest tipo GET : solicitut HTTP , para obtener un recurso del servidor del servidor.

def crea_profesor(request):
        
    if request.method == "POST" :
        
        miFormulario = ProfesorFormulario(request.POST) # Agregamos los formularios de Django.

        if miFormulario.is_valid(): # Validacion del forulario.

            data = miFormulario.cleaned_data # cleaned_da es donde se guarda la iinfo.

            profesor = Profesor(nombre=data['nombre'], apellido=data['apellido'],email=data['email'], profesion=data['profesion']) # Cargamos los datos del formulario

            profesor.save() # Guardamos el formulario.

            return redirect (inicio) # Retornamos al inicio.
         
    else:
        
            miformulario = ProfesorFormulario()
            return render (request,"profesorFormulario.html",{"miformulario": miformulario})
    
# Delete - Eliminamos un profesor de la lista.
    
def eliminarProfesor(request, id): # Eliminar un dato de la lsita,  li indicamos u
        
    if request.method == "POST" :
            
        profesor = Profesor.objects.get(id=id) # Devuelve un solo registro.

        profesor.delete() # Elimina el elemento seleccionado.

        profesores = Profesor.objects.all() # Manager para llamar a los archivos de la base de datos 'objects'.

        return render(request,'listaProfesores.html', {'profesores':profesores})
    
# Upgrade - Actualizacion.

def edita_profesor(request, id):

    profesor = Profesor.objects.get(id=id) # Devuelve un solo registro.

    if request.method == "POST" :
        
        miFormulario = ProfesorFormulario(request.POST) # Agregamos los formularios de Django.

        if miFormulario.is_valid(): # Validacion del forulario.

            data = miFormulario.cleaned_data # cleaned_da es donde se guarda la iinfo.

            profesor.nombre = data["nombre"]
            profesor.apellido = data["apellido"]
            profesor.email = data["email"]
            profesor.profesion = data["profesion"]

            profesor.save() # Guardamos el formulario.

            return redirect (inicio) # Retornamos al inicio.
         
    else:
        
        miformulario = ProfesorFormulario(initial={  # Llamamos al formulario con sus respectivas values.
            "nombre" : profesor.nombre,
            "apellido" : profesor.apellido,
            "email" : profesor.email,
            "profesion" : profesor.profesion,
        })

        return render (request,"edtarProfesor.html",{"miformulario": miformulario, "id": profesor.id})
    

# Vistas basadas en Clases.
# CRUD  Creat - Read - Upgrade - Delet

# Listado - Genera la lista de cursos.

class CursoList(ListView):

    model = Curso # De donde xportamos los datos.
    template_name = "curso_lista.html"
    # Definimos el nombre del contexto para luego recorrer.
    context_object_name ='cursos'

# Detail del curso.

class CursoDetail(DetailView):

    model = Curso # De donde xportamos los datos.
    template_name = "curso_detail.html"
    context_object_name ='curso'

# Create registro.

class CursoCreate(CreateView):

    model = Curso # De donde xportamos los datos.
    template_name = "curso_create.html"
    fields = ['nombre','camada']  # Los atribustos que va a poseer este lsitado.
    success_url ='/app-code/' # Dinde redirigimos una vez finalizado el creado.

# Update - Actualziacion de dados.

class CursoUpdate(UpdateView):

    model = Curso # De donde xportamos los datos.
    template_name = "curso_update.html"
    fields = ('__all__')  #['nombre','camada']  # Los atribustos que va a poseer este lsitado. Se puede indicar los campos o llamar todos.
    success_url ='/app-code/' # Donde redirigimos una vez finalizado el creado.
    
# Delte - Eliminar

class CursoDelete(DeleteView):

    model = Curso # De donde xportamos los datos.
    template_name = "curso_delete.html" # Django nos obliaga a una confirmacion de la eliminacion.
    success_url = '/app-code/'

    