from django.contrib import admin
from .models import Curso, Categoria_curso

# Register your models here.

admin.site.register(Categoria_curso)
admin.site.register(Curso)

