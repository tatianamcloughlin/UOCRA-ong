from tkinter import CASCADE
from django.db import models
from ckeditor.fields import RichTextField


class Categorias(models.Model):
    nombre = models.CharField(max_length=50,null=False)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

# Create your models here.

class Noticias(models.Model):
    categoria = models.ForeignKey(Categorias,null=True,on_delete=models.CASCADE)
    titulo = models.CharField(max_length=250, null =False)
    introduccion = models.TextField(max_length=100, null =True)    
    fecha = models.DateTimeField(auto_now=True)
    texto = models.TextField(max_length=1300, null= True)
    activo = models.BooleanField( default =True)
    imagenes = models.ImageField(upload_to="noticias/",null=True)



  