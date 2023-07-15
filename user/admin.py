from django.contrib import admin
from django.contrib.auth import get_user_model
User = get_user_model()

# Registrando los modelos de Animal y Categoria para que sean
# administrados.

admin.site.register(User)
