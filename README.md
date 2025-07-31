# 🌟 Portafolio Personal - Diana Jiménez

Este proyecto es un **portafolio web personal** desarrollado con **Python** y **Django**. Permite mostrar tus proyectos, habilidades técnicas y blandas, experiencia laboral, estudios y hobbies, así como recibir mensajes de contacto. Es ideal para presentar tu perfil profesional de forma moderna y administrable.

---

## 🚀 Instalación paso a paso

### 1. Clona el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd proyecto-portafolio
```

### 2. Crea y activa un entorno virtual

#### En Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### En Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instala las dependencias

```bash
pip install django
```

### 4. Prepara la base de datos

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Crea un usuario administrador

```bash
python manage.py createsuperuser
```

Sigue las instrucciones para usuario, correo y contraseña.

### 6. Inicia el servidor de desarrollo

```bash
python manage.py runserver
```

### 7. Accede desde el navegador

- Portafolio: http://127.0.0.1:8000/
- Panel admin: http://127.0.0.1:8000/admin/

---

## 🗂️ Estructura del proyecto

```
proyecto-portafolio/
│
├── portafolio/                # Configuración principal del proyecto Django (urls.py, settings.py, etc)
├── portafolio_app/            # App principal: modelos, vistas, formularios, templates
│   ├── models.py              # Modelos: Proyecto, Habilidad, Experiencia, Estudio, Hobby, Contacto
│   ├── views.py               # Lógica de vistas (CRUD y páginas principales)
│   ├── forms.py               # Formularios para cada modelo
│   ├── urls.py                # Rutas específicas de la app
│   └── templates/portafolio/  # Templates HTML organizados por funcionalidad
│
├── static/                    # Archivos estáticos: CSS, imágenes, JS
│   └── css/
│   └── img/
│
├── manage.py
└── README.md
```

---

## 🧠 Lógica clave y funcionamiento

- **portafolio_app** es la app principal. Aquí están los modelos, vistas y formularios.
- **Modelos**: Definen la estructura de los datos (proyectos, habilidades, etc).
- **Vistas (`views.py`)**: Cada sección (proyectos, experiencia, estudios, hobbies, habilidades, contacto) tiene vistas CRUD (crear, leer, actualizar, eliminar). También hay vistas para mostrar el portafolio y la página de contacto.
- **Formularios**: Se usan para crear y editar cada entidad desde el panel de administración o desde la web.
- **Templates**: HTML organizado para cada sección, usando Bootstrap para el diseño.
- **Rutas**: `portafolio/urls.py` conecta la raíz y el admin; `portafolio_app/urls.py` define las rutas de cada sección.

### Flujo típico

1. El usuario navega por las secciones del portafolio (sobre mí, proyectos, experiencia, etc).
2. El administrador puede agregar, editar o eliminar información desde la web o el panel `/admin/`.
3. Los visitantes pueden enviar mensajes desde la página de contacto.

---

## 🛠️ Administración

- Accede a `/admin/` con tu usuario admin para gestionar todo el contenido fácilmente.
- También puedes usar los formularios web para CRUD de cada sección.

---

## 📚 Personalización

- Modifica los estilos en `static/css/styles.css` y otros archivos CSS para cambiar colores y diseño.
- Cambia imágenes en `static/img/`.
- Los textos y secciones se pueden editar desde el panel admin o los formularios web.

---

## 💡 Notas

- El proyecto está pensado para ser fácil de mantener y ampliar.
- Puedes agregar más modelos o secciones según tus necesidades.
- El código está comentado para facilitar la comprensión y personalización.


