from django.db import models
from django.contrib.auth.models import User

class Personaje(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=100)
    nivel = models.IntegerField()
    clase = models.CharField(max_length=100)
    especializacion = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='personajes/')
    imagen3d = models.FileField(upload_to='personajes/',blank=True)

    def __str__(self):
        return self.nombre