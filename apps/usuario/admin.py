from django.contrib import admin

# Register your models here.
from .models import UsuarioManager,Usuario

 

admin.site.register(Usuario)