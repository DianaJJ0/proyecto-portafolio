from django.contrib import admin
from .models import Proyecto, Habilidad,Estudio,ExperienciaLaboral,Hobby # 1. Importa proyecto y Habilidad

# Register your models here.
admin.site.register(Proyecto)
admin.site.register(Habilidad) 
admin.site.register(Hobby)
admin.site.register(Estudio)
admin.site.register(ExperienciaLaboral)   