# Archivo de rutas de la aplicación portafolio_app
# Carpeta: proyecto-portafolio/portafolio_app/

from django.urls import path
from portafolio_app import views  # Importa las vistas definidas en portafolio_app/views.py

urlpatterns = [
    # Página "Sobre mí"
    path('sobre-mi/', views.sobre_mi, name='sobre_mi'),

    # Página de contacto
    path('contacto/', views.contacto, name='contacto'),

    # Proyectos CRUD
    path('proyectos/', views.listaProyectos, name='listaProyectos'),
    path('proyectos/crear/', views.crear_proyecto, name='crear_proyecto'),
    path('proyectos/editar/<int:pk>/', views.editar_proyecto, name='editar_proyecto'),
    path('proyectos/eliminar/<int:pk>/', views.eliminar_proyecto, name='eliminar_proyecto'),

    # Experiencia Laboral CRUD
    path('experiencia/', views.lista_experiencia, name='lista_experiencia'),
    path('experiencia/crear/', views.crear_experiencia, name='crear_experiencia'),
    path('experiencia/editar/<int:pk>/', views.editar_experiencia, name='editar_experiencia'),
    path('experiencia/eliminar/<int:pk>/', views.eliminar_experiencia, name='eliminar_experiencia'),

    # Estudios CRUD
    path('estudios/', views.lista_estudios, name='lista_estudios'),
    path('estudios/crear/', views.crear_estudio, name='crear_estudio'),
    path('estudios/editar/<int:pk>/', views.editar_estudio, name='editar_estudio'),
    path('estudios/eliminar/<int:pk>/', views.eliminar_estudio, name='eliminar_estudio'),

    # Hobbies CRUD
    path('hobbies/', views.lista_hobbies, name='lista_hobbies'),
    path('hobbies/crear/', views.crear_hobby, name='crear_hobby'),
    path('hobbies/editar/<int:pk>/', views.editar_hobby, name='editar_hobby'),
    path('hobbies/eliminar/<int:pk>/', views.eliminar_hobby, name='eliminar_hobby'),

    # Habilidades Técnicas CRUD
    path('habilidades/', views.lista_habilidades, name='lista_habilidades'),
    path('habilidades/crear/', views.crear_habilidad, name='crear_habilidad'),
    path('habilidades/editar/<int:pk>/', views.editar_habilidad, name='editar_habilidad'),
    path('habilidades/eliminar/<int:pk>/', views.eliminar_habilidad, name='eliminar_habilidad'),

    # Habilidades Blandas CRUD
    path('habilidades-blandas/', views.lista_habilidades_blandas, name='lista_habilidades_blandas'),
    path('habilidades-blandas/crear/', views.crear_habilidad_blanda, name='crear_habilidad_blanda'),
    path('habilidades-blandas/editar/<int:pk>/', views.editar_habilidad_blanda, name='editar_habilidad_blanda'),
    path('habilidades-blandas/eliminar/<int:pk>/', views.eliminar_habilidad_blanda, name='eliminar_habilidad_blanda'),
]
# Comentarios clave:
# - Cada ruta está conectada directamente a una función en portafolio_app/views.py.

# - El 'name' permite usar {% url 'nombre' %} en tus templates para navegar.

# - Aquí NO debes importar ni incluir el archivo de rutas del proyecto.

# - Este archivo solo contiene rutas de la app.
