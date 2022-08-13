from genericpath import isfile
from tkinter import CASCADE
from django.db import models
import os
# Create your models here.
class Categoria(models.Model):
    categoria = models.CharField(max_length=50)
    def __str__(self):
        return self.categoria

class Noticia(models.Model):
    categoria = models.ForeignKey(Categoria,null=False,on_delete=models.CASCADE)
    titulo = models.CharField(max_length=250, null =False)
    introduccion = models.TextField(max_length=100, null =True)
    texto = models.TextField (null= True)
    imagenes = models.ImageField(upload_to="noticias",null=True)
    

    introduccion_imagen_2 = models.TextField(max_length=100, null=True, blank=True)
    texto_imagen_2 = models.TextField (null=True, blank=True)
    imagenes_2 = models.ImageField(upload_to="noticias",null=True, blank=True)
    
    
    introduccion_imagen_3 = models.TextField(max_length=100, null =True, blank=True)
    texto_imagen_3 = models.TextField (null= True, blank=True)
    imagenes_3 = models.ImageField(upload_to="noticias",null=True, blank=True)
    

    introduccion_imagen_4 = models.TextField(max_length=100, null =True, blank=True)
    texto_imagen_4 = models.TextField (null= True, blank=True)
    imagenes_4 = models.ImageField(upload_to="noticias",null=True, blank=True)
    
    
    activo = models.BooleanField( default =False)
    fecha = models.DateTimeField(auto_now=False)
    
    def delete(self, *args, **kwargs):
        if os.path.isfile(self.imagenes.path):
            os.remove(self.imagenes.path)
        super(Noticia,self).delete(*args, **kwargs)
    
    def __str__(self):
        return self.titulo
    

  