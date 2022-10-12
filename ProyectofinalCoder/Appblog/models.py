from django.db import models

# Create your models here.


class Autor(models.Model):
    class Meta:
        verbose_name_plural = "Autores"

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    profesion = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre, self.apellido


class Seccion(models.Model):
    class Meta:
        verbose_name_plural = "Secciones"

    clase = models.CharField(max_length=150)
    fecha = models.CharField(max_length=150)


class Articulo(models.Model):
    def __str__(self):
        return self.titulo, self.fecha

    titulo = models.CharField(max_length=150)
    texto = models.CharField(max_length=150)
    fecha = models.CharField(max_length=150)
