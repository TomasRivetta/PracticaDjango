from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField()
    profesor = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre + " - " + str(self.comision) + " - " + self.profesor

class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre + " - " + self.apellido + " - " + self.email + " - " + self.profesion

class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.nombre + " - " + self.apellido + " - " + self.email

class Entregable(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_entrega = models.CharField(max_length=50)
    entregado = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre + " - " + self.fecha_entrega + " - " + self.entregado