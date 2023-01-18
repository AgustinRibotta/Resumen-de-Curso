from django.contrib import admin
from .models import Curso, Estudiante, Profesor


# Register your models here.
# De esta manera registramos nuestros modelos.

admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Profesor)

