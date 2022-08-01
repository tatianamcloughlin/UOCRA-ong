from django.db import models

# Create your models here.
class Categorias(models.Model):
    categoria = models.CharField(max_length=50,verbose_name="categoria")
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.categoria