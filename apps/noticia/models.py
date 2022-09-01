from django.db import models
from ckeditor.fields import RichTextField
from apps.usuario.models import Usuario



class Categoria(models.Model):
    nombre = models.CharField(max_length=50,null=False)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

# Create your models here.

class Noticia(models.Model):
    categoria = models.ForeignKey(Categoria,null=True,on_delete=models.CASCADE)
    titulo = models.CharField(max_length=250, null =False)
    introduccion = models.TextField(max_length=100, null =True)    
    fecha = models.DateTimeField(auto_now=True)
    texto = RichTextField(null= True)
    activo = models.BooleanField( default =True)
    imagen = models.URLField(max_length=1050, null=False)

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    usuario = models.ForeignKey(Usuario, null=True, on_delete= models.SET_NULL)
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)
    comentario = models.TextField()
    fecha = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.comentario



  