from django.urls import path
from BlogBuster.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('about/', about, name="About"),

    # Login
    path('login/', iniciar_sesion, name="Login"),
    path('failedlogin/', failed_login, name="LoginFailed"),
    path('logout', LogoutView.as_view(template_name="BlogBuster/login/logout.html"), name="Logout"),

    # Logout
    path('register/', register, name="LoginRegister"),
    path('userregistered/', registered_ok, name="LoginRegisterOk"),
    
    # Profile 
    path('editprofile/', editarPerfil, name="EditarPerfil"),
    path('addavatar/', agregarAvatar, name="AgregarAvatar"),

    # Búsqueda Y Resultados (VHS)
    path('searchvhs/', searchVhs, name="SearchVhs"),
    path('resultadoVhs/', resultadoVhs),
    
    # Búsqueda Y Resultados (CDs)
    path('searchcds/', searchCds, name="SearchCds"),
    path('resultadoCds/', resultadoCds),

    # Búsqueda Y Resultados (Juegos)
    path('searchvideojuegos/', searchJuegos, name="SearchJuegos"),
    path('resultadoVideojuegos/', resultadoVideojuegos),

    #CRUD de VHS usando clases
    path('vhs/list/', ListaVhs.as_view(), name="ListaVhs"),
    path('vhs/<int:pk>/', DetalleVhs.as_view(), name="DetalleVhs"),
    path('vhs/cargar/', cargarVhs, name="CargarVhs"),
    path('vhs/editar/<int:pk>/', UpdateVhs.as_view(), name="UpdateVhs"),
    path('vhs/borrar/<int:pk>/', DeleteVhs.as_view(), name="DeleteVhs"),

    #CRUD de CDs usando clases
    path('cds/list/', ListaCds.as_view(), name="ListaCds"),
    path('cds/<int:pk>/', DetalleCds.as_view(), name="DetalleCds"),
    path('cds/cargar/', CargarCds.as_view(), name="CargarCds"),
    path('cds/editar/<int:pk>/', UpdateCds.as_view(), name="UpdateCds"),
    path('cds/borrar/<int:pk>/', DeleteCds.as_view(), name="DeleteCds"),

    #CRUD de Juegos usando clases
    path('juegos/list/', ListaJuegos.as_view(), name="ListaJuegos"),
    path('juegos/<int:pk>/', DetalleJuegos.as_view(), name="DetalleJuegos"),
    path('juegos/cargar/', CargarJuegos.as_view(), name="CargarJuegos"),
    path('juegos/editar/<int:pk>/', UpdateJuegos.as_view(), name="UpdateJuegos"),
    path('juegos/borrar/<int:pk>/', DeleteJuegos.as_view(), name="DeleteJuegos"),
]


