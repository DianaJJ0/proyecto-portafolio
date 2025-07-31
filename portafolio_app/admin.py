from django.contrib import admin
from .models import Proyecto, ExperienciaLaboral, Estudio, Hobby, Habilidad, HabilidadBlanda, Contacto

# Registro de modelos en el panel de administración de Django

admin.site.register(Proyecto)
admin.site.register(ExperienciaLaboral)
admin.site.register(Estudio)
admin.site.register(Hobby)
admin.site.register(Habilidad)
admin.site.register(HabilidadBlanda)
admin.site.register(Contacto)
