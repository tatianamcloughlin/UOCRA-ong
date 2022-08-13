from django.urls import path


from . import views

app_name = 'apps.cursos'

urlpatterns = [
    path('<str:nombre>', views.curso, name='curso' ),
    path('galeria/<str:nombre>', views.ListaFotosPorCurso, name="galeria"),
    path('cursos/addFotos', views.addFotos.as_view(), name='addFotos' ),
    path('cursos/galeria', views.MostrarGaleria, name='gal'),

  
]