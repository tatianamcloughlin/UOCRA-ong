from django.urls import path


from . import views

app_name = 'apps.noticia'

urlpatterns = [
    path('noticia/listaNoticias', views.MostrarNoticia, name='lista'),
    path('<str:categoria>', views.ListarNoticiaPorCategoria, name="listaNoticias"),
    path('noticia/<int:id>', views.noticia, name= 'noticia'),
]