from django.db import models

class Clase(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    

class Especializacion(models.Model):
    nombre = models.CharField(max_length=50)
    ref_clase = models.ForeignKey(Clase, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class EstadoProducto(models.Model):

    estado = models.CharField(max_length=50)

    def __str__(self):
        return self.estado

class Producto(models.Model):
    ref_especializacion = models.ForeignKey(Especializacion, on_delete=models.CASCADE)
    ref_estado = models.ForeignKey(EstadoProducto, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=400)
    caracteristicas = models.CharField(max_length=400)
    precio = models.IntegerField()
    fecha_creacion = models.DateTimeField()
    imagen = models.FileField(upload_to='productos/')
