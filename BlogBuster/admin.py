from django.contrib import admin
from BlogBuster.models import *
from .models import *

# Register your models here.
admin.site.register(Vhs)
admin.site.register(Cds)
admin.site.register(Videojuegos)
admin.site.register(Avatar)