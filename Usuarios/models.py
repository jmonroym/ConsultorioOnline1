from django.db import models
from django.db.models.fields import CharField   

class Proveedor(models.Model):
    usuario = models.CharField(max_length=200) 
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    compania = models.CharField(max_length=200)

    def __str__(self):
        return ('Username: ' + self.usuario + ', compania: ' + self.compania)
 