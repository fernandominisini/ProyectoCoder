from django.shortcuts import render
from accounts.forms import *
from accounts.models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.




def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            info=form.cleaned_data
            
            usu=info["username"]
            clave=info["password"]
            usuario=authenticate(username=usu, password=clave) 
            
            if usuario is not None:
                login(request, usuario)
                return render(request, "BlogRiverPlate/inicio.html", {"mensaje":f"Usuario {usu} logueado correctamente!", "avatar":obtenerAvatar(request)})
            else:
                return render(request, "BlogRiverPlate/login.html", {"form": form, "mensaje":"Usuario o contraseña incorrectos"})
        else:
            return render(request, "BlogRiverPlate/login.html", {"form": form, "mensaje":"Usuario o contraseña incorrectos"})
    else:
        form=AuthenticationForm()
        return render(request, "BlogRiverPlate/login.html", {"form": form})     


def register(request):
    if request.method=="POST":
        form= RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get("username")
            form.save()
            return render(request, "BlogRiverPlate/login.html", {"mensaje":f"Usuario {username} registrado correctamente!", "avatar":obtenerAvatar(request)})
        else:
            return render(request, "BlogRiverPlate/register.html", {"form": form, "mensaje":"Error al crear el usuario"})
    else:
        form = RegistroUsuarioForm()
        return render(request, "BlogRiverPlate/register.html", {"form": form})

@login_required
def obtenerAvatar(request):

    avatares=Avatar.objects.filter(user=request.user.id)
    if len(avatares)!=0:
        return avatares[0].imagen.url
    else:
        return "/media/avatars/default.png"

@login_required
def verPerfil(request):

    return render(request, "accounts/perfilDeUsuario.html", {"avatar":obtenerAvatar(request)})


@login_required
def editarPerfilUsuario(request):
    usuario=request.user

    if request.method=="POST":
        form=UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.save()
            return render(request, "BlogRiverPlate/inicio.html", {"mensaje":f"Usuario {usuario.username} editado correctamente", "avatar":obtenerAvatar(request)})
        else:
            return render(request, "accounts/editarPerfilUsuario.html", {"form": form, "nombreusuario":usuario.username, "avatar":obtenerAvatar(request)})
    else:
        form=UserEditForm(instance=usuario)
        return render(request, "accounts/editarPerfilUsuario.html", {"form": form, "nombreusuario":usuario.username, "avatar":obtenerAvatar(request)})

@login_required
def crearBlog(request):

    if request.method == "POST":

        form=BlogCreadoForm(request.POST)

        if form.is_valid():
            
            info=form.cleaned_data

            blog=BlogCreado(tituloDelBlog=info["tituloDelBlog"], subtituloDelBlog=info["subtituloDelBlog"], cuerpoDelBlog=info["cuerpoDelBlog"],
            autorDelBlog=info["autorDelBlog"], fechaDelBlog=info["fechaDelBlog"]) 
            blog.save()
            return render(request, "BlogRiverPlate/inicio.html", {"mensaje":f"Blog {blog.tituloDelBlog} creado correctamente", "avatar":obtenerAvatar(request)})
        else:
            return render(request, "accounts/crearBlog.html", {"form": form, "mensaje":"Error al crear el blog", "avatar":obtenerAvatar(request)})

    else:

        form = BlogCreadoForm()
    blogs = BlogCreado.objects.all()    
    context = {"blogs" : blogs, "form" : form, "avatar":obtenerAvatar(request)}
    return render(request, "accounts/crearBlog.html", context)


@login_required
def listaDeBlogs(request):

    form = BlogCreadoForm(request.POST)
    blogs = BlogCreado.objects.all()   
    context = {"blogs": blogs, "form": form, "avatar":obtenerAvatar(request)} 
    return render(request, "accounts/listaDeBlogs.html",context)


@login_required
def verBlog(request, id):

    blog=BlogCreado.objects.get(id=id)
    blogs=BlogCreado.objects.filter(id__icontains=id)
    return render(request, "accounts/verBlog.html" ,{"blogs": blogs, "avatar":obtenerAvatar(request)})

        

@login_required
def agregarAvatar(request):
    if request.method=="POST":
        form=AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatar=Avatar(user=request.user, imagen=request.FILES["imagen"])
            
            avatarViejo=Avatar.objects.filter(user=request.user)
            if len(avatarViejo)>0:
                avatarViejo[0].delete()
            avatar.save()
            return render(request, "BlogRiverPlate/inicio.html", {"mensaje":f"Foto de perfil cambiada correctamente!", "avatar":obtenerAvatar(request)})
        else:
            return render(request, "accounts/editarAvatar.html", {"form": form, "usuario": request.user, "mensaje":"Error al cambiar foto de perfil", "avatar":obtenerAvatar(request)})
    else:
        form=AvatarForm()
        return render(request, "accounts/editarAvatar.html", {"form": form, "usuario": request.user, "avatar":obtenerAvatar(request)})

@login_required
def editarBlog(request, id):

    usuario=request.user
    nombreAutor=BlogCreado.objects.filter(autorDelBlog__icontains=usuario.username)
    print(nombreAutor)
    blog=BlogCreado.objects.get(id=id)

    if request.method=="POST":
        form=BlogCreadoForm(request.POST)
        if form.is_valid():
            
            info=form.cleaned_data
            blog.tituloDelBlog=info["tituloDelBlog"]
            blog.subtituloDelBlog=info["subtituloDelBlog"]
            blog.cuerpoDelBlog=info["cuerpoDelBlog"]
            blog.autorDelBlog=info["autorDelBlog"]
            blog.fechaDelBlog=info["fechaDelBlog"]
            

            blog.save()
            blogs=BlogCreado.objects.all()
            form = BlogCreadoForm()
            return render(request, "accounts/listaDeBlogs.html" ,{"blogs": blogs, "mensaje": "Blog editado correctamente", "form": form, "avatar":obtenerAvatar(request)})
        pass
    else:
        formulario=BlogCreadoForm(initial={"tituloDelBlog": blog.tituloDelBlog, "subtituloDelBlog": blog.subtituloDelBlog,
        "cuerpoDelBlog": blog.cuerpoDelBlog, "autorDelBlog": blog.autorDelBlog, "fechaDelBlog" : blog.fechaDelBlog})

        return render(request, "accounts/editarBlog.html", {"form": formulario, "blog": blog, "avatar":obtenerAvatar(request)})    


@login_required
def eliminarBlog(request, id):

    usuario=request.user
    nombreAutor=BlogCreado.objects.filter(autorDelBlog__icontains=usuario.username)
    print(nombreAutor)
    blog=BlogCreado.objects.get(id=id)
    print(blog)
    blog.delete()
    blogs=BlogCreado.objects.all()
    form = BlogCreadoForm()
    return render(request, "accounts/listaDeBlogs.html", {"blogs": blogs, "mensaje": "Blog eliminado correctamente", "form": form, "avatar":obtenerAvatar(request)})