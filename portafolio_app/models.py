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
# MODELO: Habilidad Técnica
# =========================
class Habilidad(models.Model):
    NIVEL_CHOICES = [
        ('basico', 'Básico'),
        ('intermedio', 'Intermedio'),
        ('avanzado', 'Avanzado'),
    ]
    nombre = models.CharField(max_length=50)
    nivel = models.CharField(max_length=20, choices=NIVEL_CHOICES)
    icono = models.CharField(max_length=50, blank=True, default="")  # icono CSS/HTML opcional

    class Meta:
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades"

    def __str__(self):
        return f"{self.nombre} ({self.get_nivel_display()})"


# =========================
# MODELO: Habilidad Blanda
# =========================
class HabilidadBlanda(models.Model):
    nombre = models.CharField(max_length=50)
    icono = models.CharField(max_length=50, blank=True, default="")  # icono CSS/HTML opcional

    class Meta:
        verbose_name = "Habilidad Blanda"
        verbose_name_plural = "Habilidades Blandas"

    def __str__(self):
        return self.nombre

# =========================
# MODELO: Experiencia Laboral
# =========================
class ExperienciaLaboral(models.Model):
    puesto = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.puesto} en {self.empresa}"


# =========================
# MODELO: Estudio
# =========================
class Estudio(models.Model):
    institucion = models.CharField(max_length=120)
    titulo_obtenido = models.CharField(max_length=120)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.titulo_obtenido} en {self.institucion}"

# =========================
# MODELO: Hobby o Pasatiempo
# =========================
class Hobby(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre
