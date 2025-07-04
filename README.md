# 🌟 Portafolio Personal - Diana Jiménez

Portafolio web personal desarrollado con Python y Django, que muestra mis proyectos, habilidades y experiencia como Diseñadora Gráfica y Desarrolladora de Software.

## 📋 Descripción

Este proyecto es un portafolio web responsive que presenta mi trabajo y habilidades profesionales. Incluye secciones para proyectos destacados, información personal, habilidades técnicas y un formulario de contacto.

## ✨ Características

- **Diseño Responsive**: Adaptable a diferentes dispositivos y tamaños de pantalla
- **Tema Oscuro**: Interfaz moderna con esquema de colores oscuros
- **Gestión de Proyectos**: Panel de administración para agregar/editar proyectos
- **Formulario de Contacto**: Funcional con validación de campos
- **Animaciones CSS**: Efectos hover y transiciones suaves
- **Bootstrap Integration**: Framework CSS para diseño responsive

## 🛠️ Tecnologías Utilizadas

- **Backend**: Django 5.2.4
- **Frontend**: HTML5, CSS3, JavaScript
- **Framework CSS**: Bootstrap 5.3.3
- **Iconos**: Bootstrap Icons
- **Base de Datos**: SQLite (por defecto)
- **Python**: 3.x

## 📁 Estructura del Proyecto

```
proyecto-portafolio/
├── portafolio_app/
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   ├── 0002_remove_proyecto_url_alter_proyecto_fecha.py
│   │   ├── 0003_habilidad.py
│   │   └── __init__.py
│   ├── templates/
│   │   └── portafolio/
│   │       ├── base.html          # Plantilla base
│   │       ├── inicio.html        # Página de inicio
│   │       ├── proyectos.html     # Galería de proyectos
│   │       ├── sobre_mi.html      # Información personal
│   │       └── contacto.html      # Formulario de contacto
│   ├── __init__.py
│   ├── admin.py                   # Configuración del panel admin
│   ├── apps.py
│   ├── forms.py                   # Formularios Django
│   ├── models.py                  # Modelos de base de datos
│   ├── tests.py
│   └── views.py                   # Vistas/controladores
├── static/
│   ├── css/
│   │   └── styles.css             # Estilos personalizados
│   └── img/
│       └── servitech_cover.png    # Imágenes del proyecto
├── proyecto_portafolio/
│   ├── __init__.py
│   ├── settings.py                # Configuración de Django
│   ├── urls.py                    # URLs principales
│   └── wsgi.py
├── manage.py                      # Comando de gestión Django
└── README.md                      # Este archivo
```

## 🚀 Instalación y Configuración

### Prerrequisitos

- Python 3.8 o superior
- Git

### Paso a Paso

1. **Clonar el repositorio**
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd proyecto-portafolio
   ```

2. **Crear un entorno virtual**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install django
   ```

4. **Configurar la base de datos**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Crear un superusuario (opcional)**
   ```bash
   python manage.py createsuperuser
   ```
   Sigue las instrucciones para crear tu usuario administrador.

6. **Ejecutar el servidor de desarrollo**
   ```bash
   python manage.py runserver
   ```

7. **Acceder a la aplicación**
   - Portafolio: http://127.0.0.1:8000/
   - Panel de administración: http://127.0.0.1:8000/admin/

## 📊 Modelos de Base de Datos

### Proyecto
```python
- titulo: CharField (máx. 100 caracteres)
- descripcion: TextField
- fecha: DateField
```

### Habilidad
```python
- nombre: CharField (máx. 50 caracteres)
- nivel: CharField con opciones (Básico, Intermedio, Avanzado)
```

## 🎨 Personalización

### Estilos
Los estilos personalizados se encuentran en `static/css/styles.css`. El archivo está organizado en secciones:
- Estilos globales y base
- Componentes reutilizables
- Estilos específicos por página

### Colores Principales
- Fondo principal: `#121212`
- Texto principal: `#ffffff`
- Texto secundario: `#cccccc`
- Acento azul: `#007bff`
- Bordes: `#444`

### Añadir Nuevos Proyectos
1. Accede al panel de administración: `/admin/`
2. Ve a la sección "Proyectos"
3. Haz clic en "Agregar proyecto"
4. Completa los campos requeridos
5. Guarda los cambios

## 🔧 Configuraciones Adicionales

### Variables de Entorno (Producción)
Para despliegue en producción, considera configurar:
- `SECRET_KEY`
- `DEBUG = False`
- `ALLOWED_HOSTS`
- Configuración de base de datos
- Configuración de archivos estáticos

### Archivos Estáticos
```python
# En settings.py
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
```

## 🤝 Contribuciones

Este es un proyecto personal, pero si tienes sugerencias o encuentras algún error, no dudes en contactarme.

## 📄 Licencia

Este proyecto está desarrollado con fines educativos y de portafolio personal.

---

⭐ **¡Gracias por visitar mi portafolio!** ⭐
