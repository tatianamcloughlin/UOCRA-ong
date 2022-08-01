from tkinter import CASCADE
from django.db import models
from apps.categoria.models import Categorias

# Create your models here.

class Noticias(models.Model):
    categoria = models.ForeignKey(Categorias,null=True,on_delete=models.CASCADE)
    introduccion = models.TextField(max_length=100, null =True)
    titulo = models.CharField(max_length=250, null =False)
    fecha = models.DateTimeField(auto_now=True)
    texto = models.TextField (null= True)
    activo = models.BooleanField( default =True)
    imagenes = models.ImageField(upload_to="noticias",null=True)
    

  