from django.urls import path, re_path
from . import views

app_name="apps.comentarios"

urlpatterns = [
    path('addcomentario/', views.AddComentario, name="addcomentario"),
    path('comentario/', views.Comentarios, name="comentario")
]