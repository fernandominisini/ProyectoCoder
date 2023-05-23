from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class BlogCreado(models.Model):
    tituloDelBlog=models.CharField(max_length=50)
    subtituloDelBlog=models.CharField(max_length=100)
    cuerpoDelBlog=models.TextField()
    autorDelBlog=models.CharField(max_length=50)
    fechaDelBlog=models.DateField()

    def __str__(self):
        return f"{self.tituloDelBlog.upper()} - {self.subtituloDelBlog}"

class Avatar(models.Model):
    imagen=models.ImageField(upload_to="avatars")
    user=models.ForeignKey(User, on_delete=models.CASCADE)         