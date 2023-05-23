from django.shortcuts import render
from django.template import loader
from .forms import RegistroUsuarioForm, UserEditForm
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from accounts.views import obtenerAvatar
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(request):
    return render(request, 'BlogRiverPlate/inicio.html',{"avatar":obtenerAvatar(request)})


def informacion(request):
    return render(request, 'BlogRiverPlate/informacion.html',{"avatar":obtenerAvatar(request)})


def login_request(request):
    if request.method == "POST":
        form=AuthenticationForm(request, data= request.POST)
        if form.is_valid():
            info= form.cleaned_data
            usu=info["username"]
            clave=info["password"]
            usuario=authenticate(username=usu, password=clave)
            
            if usuario is not None:
                login(request, usuario)
                return render(request, "BlogRiverPlate/inicio.html", {"mensaje": f"Usuario {usu} logueado correctamente","avatar":obtenerAvatar(request)})
            else:
                return render(request, "BlogRiverPlate/login.html", {"form": form, "mensaje": "Usuario o contreaseña incorrectos","avatar":obtenerAvatar(request)})
        else:
            return render(request, "BlogRiverPlate/login.html", {"form": form, "mensaje": "Usuario o contreaseña incorrectos","avatar":obtenerAvatar(request)})
    else:
        form=AuthenticationForm()
        return render(request, "BlogRiverPlate/login.html", {"form": form,"avatar":obtenerAvatar(request)})
    
def register(request):
    if request.method=="POST":
        form= RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get("username")
            form.save()
            return render(request, "BlogRiverPlate/inicio.html", {"mensaje": f"Usuario {username} creado correctamente","avatar":obtenerAvatar(request)})
        else:
            return render(request, "BlogRiverPlate/register.html", {"form": form, "mensaje": "Error al crear el usuario","avatar":obtenerAvatar(request)})
    else:
        form= RegistroUsuarioForm()
        return render(request, "BlogRiverPlate/register.html", {"form": form,"avatar":obtenerAvatar(request)})
    
 
