from turtle import update
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserChangeForm
from django.db import connection

from .models import MyUser


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    
    class Meta:
        model = MyUser
        fields = ('email', 'fecha')

    def clean_password2(self):
        # Compruebe que las dos entradas de contraseña coincidan
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        
        return password2
        
    def save(self, commit=True):
        # Guarde la contraseña proporcionada en formato hash
        
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

"""
class UserChangeForm(UserChangeForm):
   
    password = ReadOnlyPasswordHashField()             

    fila= 0
    with connection.cursor() as cursor:
        cursor.execute("SELECT restablecer FROM usuario_myuser WHERE email= 'benjidfer@gmail.com'")
        row = cursor.fetchone()
        fila = row[0]
  
    

  
class Meta:
        model = MyUser
        fields = ('email', 'password', 'fecha', 'usuario_activo', 'es_admin')

        with connection.cursor() as cursor:  
            cursor.execute(f"UPDATE usuario_myuser SET restablecer = '0' WHERE email='benjidfer@gmail.com'")
       
"""    

class UserAdmin(BaseUserAdmin):
    # Los formularios para agregar y cambiar instancias de usuario
    form = UserChangeForm
    add_form = UserCreationForm
    

    
    
    # Los campos que se utilizarán para mostrar el modelo de usuario.
    # Estos anulan las definiciones en el UserAdmin base
    # que hacen referencia a campos específicos en auth.User.
    list_display = ('email', 'fecha', 'es_admin')
    list_filter = ('es_admin',)
    
    fieldsets = (
        (None, {'fields': ('usuario','email', 'password',)}),
        ('Personal info', {'fields': ('nombre','apellido','provincia','ciudad','direccion','dni','cuil','fecha')}),
        ('Permissions', {'fields': ('usuario_activo','restablecer',)}),
    )
    # add_fieldsets no es un atributo ModelAdmin estándar. UserAdmin
    # anula get_fieldsets para usar este atributo al crear un usuario.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('nombre','apellido','provincia','ciudad','direccion','dni','cuil','usuario','email', 'password1', 'password2', 'fecha'),
        }),
    )
    
    
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()



# Ahora registre el nuevo UserAdmin ...
admin.site.register(MyUser, UserAdmin)
# ... y, dado que no usamos los permisos integrados de Django,
# anular el registro del modelo de grupo de admin.
admin.site.unregister(Group)

