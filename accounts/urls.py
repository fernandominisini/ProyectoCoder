from django.urls import path
from accounts.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path("crearBlog/", crearBlog, name="crearBlog"),
    path("listaDeBlogs/", listaDeBlogs, name="listaDeBlogs"),
    path("listaDeBlogs/<int:id>", verBlog, name="verBlog"),
    path("editarBlog/<int:id>", editarBlog, name="editarBlog"),
    path("eliminarBlog/<int:id>", eliminarBlog, name="eliminarBlog"),    
    path("iniciarSesion/", login_request, name="iniciarSesion"),
    path("registrarse/", register, name="registrarse"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("perfilDeUsuario/", verPerfil, name="perfilDeUsuario"),    
    path("editarPerfilUsuario/", editarPerfilUsuario, name="editarPerfilUsuario"),
    path("editarFotoDePerfil/", agregarAvatar, name="editarFotoDePerfil"),

]