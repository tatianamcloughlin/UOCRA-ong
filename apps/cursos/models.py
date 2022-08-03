from django.db import models

# Create your models here.

class Categorias(models.Model):
    categoria = models.CharField(max_length=50, null=False)
    

class Cursos(models.Model):
    curso = models.CharField(max_length=50, null=False)
    recursos = models.CharField(null=True)
    duracion = models.CharField(null=True)
    
