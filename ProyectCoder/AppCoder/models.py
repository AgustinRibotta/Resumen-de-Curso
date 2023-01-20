from django.db import models

# Create your models here.

class Curso(models.Model):  # De esta froma heredamos los modelos de la clase modelos. 

    nombre = models.CharField(max_length=50) # Creamo un objeto del tipo charfild.
    camada = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} - {self.camada}'

class Estudiante(models.Model):

    nombre = models.CharField(max_length=50)
    camada = models.CharField(max_length=50)
    mail = models.EmailField()

class Profesor(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nombre} - {self.apellido}'
