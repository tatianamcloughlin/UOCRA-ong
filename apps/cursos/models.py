from django.db import models

# Create your models here.

    

class Cursos(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    descripcion = models.TextField( null =True)   
    duracion = models.CharField(max_length=50,null=True)
    logo = models.ImageField(upload_to="cursos/",null=True)
    imagen = models.ImageField(upload_to="cursos/",null=True)
    
    def __str__(self):
            return self.nombre
 
class Galeria(models.Model):
    curso = models.ForeignKey(Cursos,null=True,on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="cursos/",null=True)
    fecha = models.DateTimeField(auto_now=True)
    activo = models.BooleanField( default =True)