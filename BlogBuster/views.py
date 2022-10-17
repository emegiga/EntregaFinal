from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from BlogBuster.models import *
from BlogBuster.forms import *
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.views import generic
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.db import models
from datetime import datetime
import time

# Create your views here.

# Tiempo
def showtime(request):
    current_time = datetime.now().strftime('%H:%M:%S')   
    return render(request, current_time)

# Vista de inicio
def inicio(request):
    return render(request, "BlogBuster/inicio.html")

# Vista de pagina "About us"
def about(request):
    return render(request, "BlogBuster/about.html")

## ************************ LOGIN ************************
# LOGIN
def iniciar_sesion(request):
    if request.method == "POST":    #Acción de iniciar sesión
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():         #Valida formulario
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario, password=contra)

            if user:                #Si el formulario no está vació:
                login(request, user)
                return render(request, "BlogBuster/inicio.html", {"mensaje":f"Hola {user}"})
        else:
            return render(request, "BlogBuster/login/login_failed.html", {"mensaje":f"Los datos ingresados son incorrectos..."})
    else: 
        form = AuthenticationForm()
    return render(request, "BlogBuster/login/login.html", {"formulogin":form})

def failed_login(request):
    return render(request, "BlogBuster/login/login.html")

# Registrar usuario
def register(request):
    if request.method=="POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "BlogBuster/registro_exito.html", {"mensaje":"Usuario registrado exitosamente."})
    else:
        form  = UserRegisterForm
    return render(request, "BlogBuster/registro.html", {"formreg":form})

# Usuario registrado
@login_required 
def registered_ok(request):
    return render(request, "BlogBuster/registro_exito.html")

# Editar Usuario
@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        formprofile = UserEditForm(request.POST)
        if formprofile.is_valid:
            informacion = formprofile.cleaned_data
            usuario.email = informacion["email"]
            usuario.password1 = informacion["password1"]
            usuario.password2 = informacion["password1"]
            usuario.save()
            return render(request, "BlogBuster/registro_exito.html", {"mensaje":"Los cambios han sido guardados."})
    else:
        formprofile = UserEditForm(initial={"email":usuario.email})
    return render(request, "BlogBuster/profile_edit.html", {"formprofile":formprofile, "usuario":usuario})

# Agregar avatar
@login_required 
def agregarAvatar(request):
    if request.method == "POST":
        formavatarprofile = AvatarForm(request.POST, request.FILES)
        if formavatarprofile.is_valid():
            usuarioActual = User.objects.get(username=request.user)
            avatar = Avatar(user=usuarioActual, imagen=formavatarprofile.cleaned_data["imagen"])
            avatar.save()
            return render(request, "BlogBuster/profile_edit.html", {"mensaje":"Los cambios han sido guardados."})
    else:
        formavatarprofile = AvatarForm()
    return render(request, "BlogBuster/profile_agregarAvatar.html", {"formavatarprofile":formavatarprofile})

# class AgregarAvatar(generic.UpdateView):
#     model = Avatar
#     template_name = "BlogBuster/profile_agregarAvatar.html"
#     fields = ["imagen"]
#     success_url = "/blogbuster/editprofile/"


## ************************ BUSQUEDA Y RESULTADOS ************************
#VHS
def searchVhs(request):
    return render(request, "BlogBuster/search/vhs/buscarVhs.html")

def resultadoVhs(request):
    if request.GET["titulo"]:
        busqueda = request.GET["titulo"]
        vhs = Vhs.objects.filter(titulo__icontains=busqueda)
        return render(request, "BlogBuster/search/vhs/resultadosVhs.html", {"vhs":vhs, "busqueda":busqueda})
    else:
        mensaje = "No enviaste datos."
    return render(mensaje)  

#CDs
def searchCds(request):
    return render(request, "BlogBuster/search/cds/buscarCds.html")

def resultadoCds(request):
    if request.GET["artista"]:
        busqueda = request.GET["artista"]
        discos = Cds.objects.filter(artista__icontains=busqueda)
        return render(request, "BlogBuster/search/cds/resultadosCds.html", {"discos":discos, "busqueda":busqueda})
    else:
        mensaje = "No enviaste datos."
    return render(mensaje)

#Juegos
def searchJuegos(request):
    return render(request, "BlogBuster/search/games/buscarVideojuegos.html")

def resultadoVideojuegos(request):
    if request.GET["nombre"]:
        busqueda = request.GET["nombre"]
        juegos = Videojuegos.objects.filter(nombre__icontains=busqueda)
        return render(request, "BlogBuster/search/games/resultadosVideojuegos.html", {"juegos":juegos, "busqueda":busqueda})
    else:
        mensaje = "No enviaste datos."
    return render(mensaje)  


## ************************ CRUD de VHS (usando clases) ************************
class ListaVhs(ListView):
    model = Vhs

class DetalleVhs(DetailView):
    model = Vhs

# class CargarVhs(LoginRequiredMixin, CreateView):
#     model = Vhs
#     success_url = "/blogbuster/vhs/list" 
#     fields = ["titulo", "genero", "anioLanzamiento", "director", "imagen"]
@staff_member_required
@login_required 
def cargarVhs(request):
    if request.method == "POST":
        miFormulario = FormVHS(request.POST, request.FILES)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            vhs  = Vhs(titulo=informacion['titulo'],genero=informacion['genero'],anioLanzamiento=informacion['anioLanzamiento'],director=informacion['director'],imagen=informacion['imagen']) 
            vhs.save()
            return render(request, "BlogBuster/inicio.html")
    else:
        miFormulario= FormVHS()
    return render(request, "BlogBuster/peliculas/vhs_form.html",{'form':miFormulario})

class UpdateVhs(PermissionRequiredMixin, UpdateView):
    permission_required = "vhs.change_vhs"
    model = Vhs
    success_url = "/blogbuster/peliculas/vhs/list"
    fields = ["imagen", "titulo", "genero", "anioLanzamiento", "director"]

class DeleteVhs(PermissionRequiredMixin, DeleteView):
    permission_required = "vhs.delete_vhs"
    model = Vhs
    success_url = "/blogbuster/peliculas/vhs/list"


## ************************ CRUD de CDs (usando clases) ************************
class ListaCds(ListView):
    model = Cds

class DetalleCds(DetailView):
    model = Cds

class CargarCds(PermissionRequiredMixin, CreateView):
    permission_required = "cds.add_cds"
    model = Cds
    success_url = "/blogbuster/cds/list" 
    fields = ["nombre", "artista", "anioLanzamiento", "genero"]

class UpdateCds(PermissionRequiredMixin, UpdateView):
    permission_required = "cds.change_cds"
    model = Cds
    success_url = "/blogbuster/cds/list"
    fields = ["nombre", "artista", "anioLanzamiento", "genero"]

class DeleteCds(PermissionRequiredMixin, DeleteView):
    permission_required = "cds.delete_cds"
    model = Cds
    success_url = "/blogbuster/cds/list"


## ************************ CRUD de Juegos (usando clases) ************************
class ListaJuegos(ListView):
    model = Videojuegos

class DetalleJuegos(DetailView):
    model = Videojuegos

class CargarJuegos(PermissionRequiredMixin, CreateView):
    permission_required = "videojuegos.add_videojuegos"
    model = Videojuegos
    success_url = "/blogbuster/juegos/list" 
    fields = ["nombre", "desarrolladora", "plataforma", "genero"]

class UpdateJuegos(PermissionRequiredMixin, UpdateView):
    permission_required = "videojuegos.change_videojuegos"
    model = Videojuegos
    success_url = "/blogbuster/juegos/list"
    fields = ["nombre", "desarrolladora", "plataforma", "genero"]

class DeleteJuegos(PermissionRequiredMixin, DeleteView):
    permission_required = "videojuegos.delete_videojuegos"
    model = Videojuegos
    success_url = "/blogbuster/juegos/list"

