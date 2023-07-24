from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('registro',views.registro,name='registro'),
    path('personajes/',views.personajes, name='personajes'),
    path('crearPj/',views.crearPersonaje, name='crearPersonaje'),
    path('clases/',views.clases, name='clases'),
    path('resumen/',views.resumen, name='resumen'),
    path('mundoabierto/',views.mundoabierto, name='mundoabierto'),
    path('jugabilidad/',views.jugabilidad, name='jugabilidad'),
    path('jdestacados/',views.jdestacados, name='jdestacados'),
    path('historia/',views.historia, name='historia'),
    path('noticas/',views.noticias, name='noticias'),
    path('esports/',views.esports, name='esports'),
    path('gsotorneos/',views.gsotorneos, name='gsotorneos'),
    path('nprgeuntas/',views.preguntas, name='preguntas'),
]