# Archivo de rutas principal del PROYECTO
# Carpeta: proyecto-portafolio/proyecto-portafolio/

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    # Redirige la raíz "/" a la vista 'sobre_mi' definida en portafolio_app.urls
    path('', RedirectView.as_view(pattern_name='sobre_mi', permanent=False), name='redirect-root'),

    # Incluye todas las rutas de la app 'portafolio_app'
    path('', include('portafolio_app.urls')),

    # Admin de Django
    path('admin/', admin.site.urls),
]
