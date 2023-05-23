from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUsuarioForm(UserCreationForm):
    first_name=forms.CharField(label="Nombre")
    last_name=forms.CharField(label="Apellido")
    email=forms.EmailField(label="Email usuario")
    password1=forms.CharField(label="Contrasena", widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirmar contrasena", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=["username","first_name", "last_name", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    first_name=forms.CharField(label="Modificar nombre")
    last_name=forms.CharField(label="Modificar apellido")
    email=forms.EmailField(label="Modificar email usuario")
    password1=forms.CharField(label="Cambiar contrasena", widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirmar contrasena", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=["first_name", "last_name", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}

class UsuarioRegistradoForm(forms.Form):
    nombreDeUsuario=forms.CharField(max_length=20)
    contrasena=forms.CharField(max_length=50)
    email=forms.EmailField()

class BlogCreadoForm(forms.Form):
    tituloDelBlog=forms.CharField(max_length=50, label="Titulo")
    subtituloDelBlog=forms.CharField(max_length=100, label="Subtitulo")
    cuerpoDelBlog=forms.CharField(widget=forms.Textarea)
    autorDelBlog=forms.CharField(max_length=50, label= "Autor")
    fechaDelBlog=forms.DateField(label= "Fecha de hoy")

class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")    