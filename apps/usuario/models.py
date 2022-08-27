from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.contrib.auth.hashers import make_password
class UsuarioManager(BaseUserManager):
  
    def create_user(self, email, fecha, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            fecha=fecha,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, fecha, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            fecha=fecha,
        )
        user.es_admin = True
        user.save(using=self._db)
        return user


class Usuario(AbstractBaseUser):
    
    nombre= models.CharField('Nombre/s',max_length=100,null=True)
    apellido = models.CharField('Apellido/s',max_length=100,null=True)
    email = models.EmailField(  
        verbose_name='Correo electronico',
        max_length=255,
        unique=True,
    )
    provincia= models.CharField('Provincia',max_length=100,null=True)
    ciudad= models.CharField('Ciudad',max_length=100,null=True)
    dni=models.BigIntegerField('DNI',null=True)
    cuil=models.BigIntegerField('Cuil',null=True)
    usuario= models.CharField('Nombre usuario',max_length=100,null=True)
    direccion=models.CharField('Dirección',max_length=100,null=True)
    fecha = models.DateField()
    usuario_activo = models.BooleanField(default=True)
    restablecer = models.BooleanField(default=False)
    es_admin = models.BooleanField(default=False)
    
    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fecha']

    def __str__(self):

        if self.restablecer:
            
            self.password=f"{make_password('{}'.format(self.dni))}"
            self.restablecer=False
            self.save()
            print(self.password)
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Respuesta más simple posible: Sí, siempre
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Respuesta más simple posible: Sí, siempre
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Respuesta más simple posible: todos los administradores son personal
        return self.es_admin
    