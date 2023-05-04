from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Jugador(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    posicion=models.CharField(max_length=50)
    def __str__(self):
        return f"{self.nombre}   {self.apellido}  -  {self.posicion}"