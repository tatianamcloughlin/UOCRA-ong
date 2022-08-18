import imp
from locale import normalize
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User

 
# Create your models here.

class UsuarioManager ( BaseUserManager):
    def create_user ( self, email, username, nombres, apellidos, password = None):
        if not email:
            raise ValueError ('debe ingresar un usuario valido')

        usuario = self.model(
            username = username,
            email = self.normalize_email (email),
            nombres = nombres,
            apellidos = apellidos,)

        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser (self, email, username, nombres, apellidos, password):
        usuario = self.create_user(
            email,
            username = username,  
            nombres = nombres,
            apellidos = apellidos,
        )

        usuario.usuario_administrador = True
        usuario.save()
        return usuario


class Usuario (AbstractBaseUser):
    nombres = models.CharField(max_length=250, null =True)
    apellidos = models.CharField(max_length=250, null =True)
    provincia = models.CharField(max_length=250, null =True)
    ciudad = models.CharField(max_length=250, null =True)
    direccion = models.CharField(unique = True, max_length=250, null =True)
    dni = models.CharField(max_length=250, null =True)
    cuilcuit= models.CharField(max_length=250, null =True)
    email = models.CharField(max_length=250, null =True)
    username= models.CharField(unique=True, max_length=250, null =True)  
    fecha = models.DateTimeField(auto_now=True)
    usuario_activo = models.BooleanField ( default=True)
    usuario_administrador = models.BooleanField ( default=True)
    objects= UsuarioManager ()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS= ['email', 'nombres', 'apellidos']

    def __str__(self) :
        return f'{self.nombres} . {self.apellidos}'

    def has_perm(self,perm,obj = None):
        return True

    def has_module_perms (self,app_label):
        return True 
    
    @property
    def is_staff (self):
        return self.usuario_administrador


