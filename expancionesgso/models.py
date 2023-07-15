from django.db import models

# Create your models here.

class Expancion(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)
    precio=models.IntegerField()
    imagen = models.FileField(upload_to='expanciones/')

    def __str__(self):
        return self.nombre
