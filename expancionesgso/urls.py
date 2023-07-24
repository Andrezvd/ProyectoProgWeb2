from django.urls import path

from . import views

urlpatterns = [
#ruta vista nombre
    path('',views.expancionIndex, name='expancionIndex'),
    path('gestionEx/',views.gestionExpanciones, name='gestionExpancion'),
    path('crearEx/',views.crearExpancion, name='crearExpancion'),
    path('editarEx/<id>/',views.editarExpancion, name='editarExpancion'),
    path('borrarEx/<id>/',views.eliminarExpancion, name='eliminarExpancion'),
    path('compraEx/<id>/',views.compraExpancion, name='compraExpanciones')
]