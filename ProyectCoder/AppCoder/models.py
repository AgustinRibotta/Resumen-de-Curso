from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Curso(models.Model):  # De esta froma heredamos los modelos de la clase modelos. 

    nombre = models.CharField(max_length=50) # Creamo un objeto del tipo charfild.
    camada = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} - {self.camada}'
    
    class Meta:
        verbose_name = 'Cours' #  Modificamos los textos en el admin.
        verbose_name_plural ='My Courese'
        ordering = ['-nombre','camada']  # Ordemanamos.
        unique_together = ['nombre', 'camada'] # No permito tener los mismos valores.


class Estudiante(models.Model):

    nombre = models.CharField(max_length=50)
    camada = models.CharField(max_length=50)
    mail = models.EmailField()

    def __str__(self):
        return f'{self.nombre} - {self.camada}'


class Profesor(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)
    cusros = models.ManyToManyField(Curso, related_name='profesor_curso') # Con esto creamos una realacionde muchos a muchos.
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombre} - {self.apellido}'

# Relaciond e models
  
class Entregable(models.Model):

    nombre = models.CharField(max_length=50)
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField()
    links = models.CharField(max_length=254)
    entregable = models.ForeignKey(Estudiante, on_delete=models.CASCADE)  # Creamos la relacion 1 alumno muchos entregables.

    
# Crear los Avatars.
# Para trabajar con imagenes hay que exportar una dependencia
# En sting se deben indicar tanto MEDIA_URL:  como  MEDIA_ROOT
# Ademas ver configuracion es el url patron

class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True )


