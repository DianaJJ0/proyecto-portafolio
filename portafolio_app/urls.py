from django.contrib import admin
from django.urls import path, include
from portafolio_app import views  # Importa las vistas aquí

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),  # <-- Esta línea define la página de inicio
    path('', include('portafolio_app.urls')),
]

urlpatterns = [
    # Proyectos
    path('proyectos/', views.listaProyectos, name='listaProyectos'),
    path('proyectos/crear/', views.crear_proyecto, name='crear_proyecto'),
    path('proyectos/editar/<int:pk>/', views.editar_proyecto, name='editar_proyecto'),
    path('proyectos/eliminar/<int:pk>/', views.eliminar_proyecto, name='eliminar_proyecto'),

    # Experiencia Laboral
    path('experiencia/', views.lista_experiencia, name='lista_experiencia'),
    path('experiencia/crear/', views.crear_experiencia, name='crear_experiencia'),
    path('experiencia/editar/<int:pk>/', views.editar_experiencia, name='editar_experiencia'),
    path('experiencia/eliminar/<int:pk>/', views.eliminar_experiencia, name='eliminar_experiencia'),

    # Estudios
    path('estudios/', views.lista_estudios, name='lista_estudios'),
    path('estudios/crear/', views.crear_estudio, name='crear_estudio'),
    path('estudios/editar/<int:pk>/', views.editar_estudio, name='editar_estudio'),
    path('estudios/eliminar/<int:pk>/', views.eliminar_estudio, name='eliminar_estudio'),

    # Hobbies
    path('hobbies/', views.lista_hobbies, name='lista_hobbies'),
    path('hobbies/crear/', views.crear_hobby, name='crear_hobby'),
    path('hobbies/editar/<int:pk>/', views.editar_hobby, name='editar_hobby'),
    path('hobbies/eliminar/<int:pk>/', views.eliminar_hobby, name='eliminar_hobby'),
]