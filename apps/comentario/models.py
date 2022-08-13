from django.db import models
from apps.noticias.models import Noticias

# Create your models here.

class Comentario(models.Model):
  
    noticia = models.ForeignKey(Noticias, on_delete=models.CASCADE)
    comentario = models.TextField()
    fecha = models.DateField(auto_now_add=True)

