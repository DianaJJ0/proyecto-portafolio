from django.db import models

# =========================
# MODELO: Proyecto
# =========================
class Proyecto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateField()

    def __str__(self):
        return self.titulo

# =========================
# MODELO: Habilidad
# =========================
class Habilidad(models.Model):
    # Opciones para el campo 'nivel'
    NIVEL_CHOICES = [
        ('basico', 'Básico'),
        ('intermedio', 'Intermedio'),
        ('avanzado', 'Avanzado'),
    ]

    nombre = models.CharField(max_length=50)
    nivel = models.CharField(max_length=20, choices=NIVEL_CHOICES)

    class Meta:
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades"

    def __str__(self):
        return f"{self.nombre} ({self.get_nivel_display()})"

# =========================
# MODELO: Experiencia Laboral
# =========================
class ExperienciaLaboral(models.Model):
    puesto = models.CharField(max_length=100)  # Nombre del cargo o puesto
    empresa = models.CharField(max_length=100) # Nombre de la empresa
    fecha_inicio = models.DateField()          # Fecha de inicio
    fecha_fin = models.DateField(null=True, blank=True) # Fecha de finalización (puede estar en curso)
    descripcion = models.TextField()           # Breve descripción de tareas y logros

    def __str__(self):
        return f"{self.puesto} en {self.empresa}"

# =========================
# MODELO: Estudio
# =========================
class Estudio(models.Model):
    institucion = models.CharField(max_length=120)  # Nombre de la institución
    titulo_obtenido = models.CharField(max_length=120) # Título o grado obtenido
    fecha_inicio = models.DateField()                # Fecha de inicio
    fecha_fin = models.DateField(null=True, blank=True) # Fecha de finalización (puede estar en curso)
    descripcion = models.TextField(blank=True)       # Descripción breve (opcional)

    def __str__(self):
        return f"{self.titulo_obtenido} en {self.institucion}"


# =========================
# MODELO: Hobby o Pasatiempo
# =========================
class Hobby(models.Model):
    nombre = models.CharField(max_length=100)        # Nombre del hobby 
    descripcion = models.TextField(blank=True)       # Breve descripción (opcional)

    def __str__(self):
        return self.nombre