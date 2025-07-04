from django.contrib import admin
from .models import Proyecto, Habilidad # 1. Importa proyecto y Habilidad

# Register your models here.
admin.site.register(Proyecto)
admin.site.register(Habilidad) 