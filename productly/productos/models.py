from django.db import models
from django.utils import timezone
# Create your models here.


class Category(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Product(models.Model):
    nombre = models.CharField(max_length=255)
    stick = models.IntegerField()
    puntaje = models.FloatField()
    # CASCADE: eliminar el producto si se elimina la categoria
    # PROTECT: lanza un error
    # RESTRICT: solo elimina si no existen productos
    # SET_NULL: asigna valor a nulo
    # SET_DEFAULT: asigna valor por defecto
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    creado_en = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre
