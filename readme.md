# **PROYECTO FINAL**		
	
### Integrante: **Higa Matías**
<p>
 
  
</p>

### Comisión: **41635**
### Profesor: Juan Carlos Paredes Alva
### Tutor: Nicolás Dasanbiagio

### Instancia de Entrega: Entrega Final
<p>

</p>

---

## **INDICE:**
1. DESCRIPCION
2. ORDEN DE PRUEBA
3. FUNCIONALIDADES

---

## **1. DESCRIPCION:**

#### MODELOS:
* Vhs
* Cds
* Videojuegos
* Avatar

#### VISTAS:
* inicio
* showtime
* about
* iniciar_sesion
* failed_login
* register
* registered_ok
* editarPerfil
* agregarAvatar
* searchVhs
* resultadoVhs
* searchCds
* resultadoCds
* searchJuegos
* resultadoVideojuegos
* ListaVhs
* DetalleVhs
* cargarVhs
* UpdateVhs
* DeleteVhs
* ListaCds
* DetalleCds
* CargarCds
* UpdateCds
* DeleteCds
* ListaJuegos
* DetalleJuegos
* CargarJuegos
* UpdateJuegos
* DeleteJuegos


#### TEMPLATES:
* 400.html
* 403.html
* 404.html
* 500.hmtl
* login_failed.hmtl
* login.hmtl
* logout.hmtl
* buscarVhs.html
* buscarcds.html
* resultadoscds.hmtl
* buscarvideojuegos.hmtl
* resultadosvideojuegos.hmtl
* buscarvhs.html
* resultadosvhs.html
* inicio.html
* about.html
* padre.html
* profile_agregarAvatar.html
* profile_edit.html
* registro_exito.html
* registro.html
* vhs_confirm_delete.html
* vhs_detail.html
* vhs_list.html
* cds_detail.html
* cds_confirm_delete.html
* cds_form.html
* cds_list.html
* videojuegos_confirm_delete.html
* videojuegos_detail.html
* videojuegos_form.html
* videojuegos_list.html


APP: BlogBuster


---
## **2. ORDEN DE PRUEBA**
<p>Usuarios para prueba:</p>

* superuser: emegiga - Python-46135
* staff: gorosito - goro2022
* cliente: momo - Tito-545

<p>IMPORTANTE: Para que la carpeta media sea visible, se seteó DEBUG = False.</p>

---
## **3. FUNCIONALIDADES **
<p>FORMULARIO DE BÚSQUEDA:
<p>El formulario de búsqueda admite solamente búsquedas exactas.
Títulos de ejemplo para búsqueda:</p>

* Volver al Futuro II
* Mi Pobre Angelito
* Porco Rosso
* Matrix
* Forrest Gump</p>

#### FORMULARIOS DE CARGA:
1. CARGAR VHS: Carga de VHS en la BD, indicando título, género, año de lanzamiento y director.
2. CARGAR CDS: Carga de CD en la BD, indicando nombre, artista, año de lanzamiento y género.
3. CARGAR JUEGOS: Carga de juego en la BD, indicando nombre, empresa desarrolladora, plataforma y género.
4. REGISTRO USUARIO: Creación de usuario: Username, email, contraseña. No permite añadir avatares en nuevos usuarios (clientes).
5. EDICION USUARIO: Edición de usuario actual. Permite cargar un nuevo avatar, email y contraseña.
6. CARGA DE AVATAR: Permite crear/modificar el avatar.