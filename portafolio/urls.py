from django.contrib import admin
from django.urls import path, include  # Importa 'include' para agregar rutas de la app

urlpatterns = [
    path('admin/', admin.site.urls),  # Panel de administración

    # Incluye todas las rutas definidas en portafolio_app/urls.py en la raíz ('/')
    path('', include('portafolio_app.urls')),  # Esto permite acceder a todas las URLs de la app directamente, por ejemplo: /estudios/, /hobbies/, etc.
]