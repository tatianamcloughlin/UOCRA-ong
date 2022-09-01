from django.db import models

# Create your models here.

    

class Curso(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    descripcion = models.TextField( null =True)   
    duracion = models.CharField(max_length=50,null=True)
    logo = models.URLField(max_length=1050, null=False)
    imagen = models.URLField(max_length=1050, null=False)
    
    def __str__(self):
            return self.nombre
 
class Galeria(models.Model):
    curso = models.ForeignKey(Curso,null=True,on_delete=models.CASCADE)
    imagen = models.URLField(max_length=1050, null=False)
    fecha = models.DateTimeField(auto_now=True)
    activo = models.BooleanField( default =True)

