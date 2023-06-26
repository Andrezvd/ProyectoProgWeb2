from django.contrib import admin
from .models import Clase, Especializacion, EstadoProducto

# Registrando los modelos de Animal y Categoria para que sean
# administrados.

admin.site.register(Clase)
admin.site.register(Especializacion)
admin.site.register(EstadoProducto)