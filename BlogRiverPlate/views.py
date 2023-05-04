from django.shortcuts import render
from .models import Jugador
from .forms import JugadorForm, RegistroUsuarioForm, UserEditForm
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate

from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(request):
    return render(request, 'BlogRiverPlate/inicio.html')

def plantilla(request):
    return render(request, 'BlogRiverPlate/plantilla.html')

def informacion(request):
    return render(request, 'BlogRiverPlate/informacion.html')

def noticias(request):
    return render(request, 'BlogRiverPlate/noticias.html')


def crear_jugador(request):
    nombre_jugador="Enzo"
    apellido_jugador="Fernandez"
    posicion_jugador="5"
    
    jugador=Jugador(nombre=nombre_jugador, apellido=apellido_jugador, posicion=posicion_jugador)
    jugador.save()
    respuesta=f"Jugador creado ---- {nombre_jugador} - {apellido_jugador}"
    return HttpResponse(respuesta)


def jugadores(request):

    if request.method == "POST":
        form = JugadorForm(request.POST)
        if form.is_valid():
            jugador = Jugador()
            jugador.nombre = form.cleaned_data['nombre']
            jugador.apellido = form.cleaned_data['apellido']
            jugador.posicion = form.cleaned_data['posicion']
            
            jugador.save()
            form = JugadorForm()
    else:
        form = JugadorForm()

    jugadores = Jugador.objects.all() 

    return render(request, "BlogRiverPlate/plantilla.html", {"jugadores": jugadores, "form" : form})


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
                return render(request, "BlogRiverPlate/inicio.html", {"mensaje": f"Usuario {usu} logueado correctamente"})
            else:
                return render(request, "BlogRiverPlate/login.html", {"form": form, "mensaje": "Usuario o contreaseña incorrectos"})
        else:
            return render(request, "BlogRiverPlate/login.html", {"form": form, "mensaje": "Usuario o contreaseña incorrectos"})
    else:
        form=AuthenticationForm()
        return render(request, "BlogRiverPlate/login.html", {"form": form})
    
def register(request):
    if request.method=="POST":
        form= RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get("username")
            form.save()
            return render(request, "BlogRiverPlate/inicio.html", {"mensaje": f"Usuario {username} creado correctamente"})
        else:
            return render(request, "BlogRiverPlate/register.html", {"form": form, "mensaje": "Error al crear el usuario"})
    else:
        form= RegistroUsuarioForm()
        return render(request, "BlogRiverPlate/register.html", {"form": form})
    
 
