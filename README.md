# 🌟 Portafolio Personal - Diana Jiménez

Portafolio web desarrollado con Python y Django para mostrar proyectos, habilidades y experiencia profesional.

## 🚀 Instalación rápida en otro PC

1. **Clona el repositorio**
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd proyecto-portafolio
   ```

2. **Crea y activa un entorno virtual**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instala dependencias**
   ```bash
   pip install django
   ```

4. **Prepara la base de datos**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Crea un usuario administrador**
   ```bash
   python manage.py createsuperuser
   ```
   Ingresa usuario, correo y contraseña cuando lo solicite.

6. **Inicia el servidor**
   ```bash
   python manage.py runserver
   ```

7. **Accede desde el navegador**
   - Portafolio: http://127.0.0.1:8000/
   - Panel admin: http://127.0.0.1:8000/admin/

## 🛠️ Panel de administración

- Ingresa a `/admin/` con el usuario creado.
- Desde ahí puedes agregar, editar o eliminar proyectos, habilidades, estudios, experiencia y hobbies fácilmente.

## 📊 Modelos principales

- **Proyecto**: título, descripción, fecha
- **Habilidad**: nombre, nivel (Básico, Intermedio, Avanzado)

## 🎨 Personalización

- Edita los estilos en `static/css/styles.css` para cambiar colores y diseño.
- Las imágenes y recursos están en la carpeta `static/`.

---

⭐ **¡Listo! Ya puedes mostrar tu portafolio y administrar el contenido fácilmente.**
