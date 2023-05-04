from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', inicio, name='inicio'),
    path('plantilla/', plantilla, name='plantilla'),
    path('informacion/', informacion, name='informacion'),
    path('noticias/', noticias, name='noticias'),
    path("login/", login_request, name="login"),
    path("register/", register, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    
]