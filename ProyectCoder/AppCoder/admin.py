from django.contrib import admin
from .models import Curso, Estudiante, Profesor, Avatar, Entregable


# Register your models here.
# De esta manera registramos nuestros modelos.

class CursoAdmin(admin.ModelAdmin):  
    list_display = ['nombre', 'camada']  #  Que queremos visualisar en el admin.
    search_fields = ['nombre', 'camada'] # Campo filtadops que contengan.
    list_filter = ['nombre'] # Es un filto que te aparece en el lateral.

class ProfesorAdmin(admin.ModelAdmin):

    list_display=['nombre','apellido','email']
    list_filter = ['nombre']
    filter_horizontal=['cusros']

admin.site.register(Curso,CursoAdmin)
admin.site.register(Estudiante)
admin.site.register(Profesor,ProfesorAdmin)
admin.site.register(Avatar)
admin.site.register(Entregable)

