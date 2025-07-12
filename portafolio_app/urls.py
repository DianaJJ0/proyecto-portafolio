from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('proyectos/', views.listaProyectos, name='listaProyectos'),
    path('proyectos/', views.crear_proyecto, name='crear_proyecto'),
    path('proyectos/editar/<int:pk>', views.editar_proyecto, name='editar_proyecto'),
    path('proyectos/eliminar/<int:pk>', views.eliminar_proyecto, name='eliminar_proyecto'),






    path('sobre-mi/', views.sobre_mi, name='sobre_mi'),
    path('contacto/', views.contacto, name='contacto'),
] 