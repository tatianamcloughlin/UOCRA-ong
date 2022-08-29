from django.urls import path


from . import views

app_name = 'apps.curso'

urlpatterns = [
    path('<str:nombre>', views.curso, name='curso' ),
    path('galeria/<str:nombre>', views.ListaFotosPorCurso, name="galeria"),
    path('curso/addFotos', views.addFotos.as_view(), name='addFotos' ),
    path('curso/galeria', views.MostrarGaleria, name='gal'),

  
]