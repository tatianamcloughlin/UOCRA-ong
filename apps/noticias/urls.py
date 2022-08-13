from django.urls import path


from . import views

app_name = 'apps.noticias'

urlpatterns = [
    path('addNoticias', views.addNoticias.as_view(), name='addNoticias' ),
    path('noticias/listaNoticias', views.MostrarNoticia),
    path('<str:categoria>', views.ListarNoticiaPorCategoria, name="listaNoticias"),
    path('noticia/<int:id>', views.noticia,),
    path('eliminar/<int:id>', views.delete, name='eliminar'),
]