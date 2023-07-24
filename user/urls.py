from django.urls import path

from . import views

urlpatterns = [
    path('/ajustes/',views.ajustes, name='ajustes'),
    path('suscripcion/',views.suscripcion,name='suscripcion')
]