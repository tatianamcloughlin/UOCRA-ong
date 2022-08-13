from django.db import models

# Create your models here.
class Categoria_curso(models.Model):
    categoria = models.CharField(max_length=50)
    def __str__(self):
        return self.categoria

class Curso (models.Model):
    categoria = models.ForeignKey(Categoria_curso, null=False, on_delete=models.CASCADE)
    curso = models.CharField(max_length=50)
    profesor = models.CharField(max_length=50)
    duracion = models.CharField(max_length=100)

    def __str__(self):
        return self.curso