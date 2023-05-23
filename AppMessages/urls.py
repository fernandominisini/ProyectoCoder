from django.urls import path
from .views import *


urlpatterns = [
    
    path("", inicioMensajeria, name="inicioMensajeria"),
    path("enviarMensaje/", enviarMensaje, name="enviarMensaje"),
    path("bandejaDeEntrada/", verMensajes, name="bandejaDeEntrada"),
]