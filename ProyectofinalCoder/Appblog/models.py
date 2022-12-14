from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Subcriptores(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Autor(models.Model):
    class Meta:
        verbose_name_plural = "Autores"

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    profesion = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.apellido}, {self.profesion}"


class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    camada = models.IntegerField()
    fecha_de_inicio = models.DateField(null=True)

    def __str__(self):
        return f"{self.camada} {self.nombre}"


class Articulo(models.Model):
    def __str__(self):
        return f"{self.titulo} {self.fecha}"

    titulo = models.CharField(max_length=150)
    texto = models.CharField(max_length=150)
    fecha = models.CharField(max_length=150)


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)
