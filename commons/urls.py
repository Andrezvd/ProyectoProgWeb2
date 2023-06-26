from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('registro',views.registro,name='registro'),
    path('personajes/',views.personajes, name='personajes'),
    path('crearPj/',views.crearPersonaje, name='crearPersonaje'),
    path('clases/',views.clases, name='clases')
]