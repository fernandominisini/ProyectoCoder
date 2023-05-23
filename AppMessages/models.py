from django.db import models

# Create your models here.

class Mensaje(models.Model):
    emisor=models.EmailField()
    receptor=models.EmailField()
    cuerpoDelMensaje=models.CharField(max_length=250)

    def __str__(self):
        return f"{self.emisor} - {self.receptor} - {self.cuerpoDelMensaje}"