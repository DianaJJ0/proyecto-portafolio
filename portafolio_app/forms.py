from django import forms
from .models import Proyecto, ExperienciaLaboral, Estudio, Hobby, Habilidad, HabilidadBlanda

# =========================
# FORMULARIO: Contacto
class ContactoForm(forms.Form):
    nombre = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Tu nombre completo','class': 'form-control'}),
        label='Nombre completo'
    )
    correo = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'tu-correo@ejemplo.com','class': 'form-control'}),
        label='Correo electrónico'
    )
    asunto = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'placeholder': 'Asunto del mensaje','class': 'form-control'}),
        label='Asunto'
    )
    mensaje = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Escribe tu mensaje aquí...','class': 'form-control','rows': 5}),
        label='Mensaje'
    )

# =========================
# FORMULARIO: Proyecto
class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['titulo', 'descripcion', 'fecha']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
        }

# =========================
# FORMULARIO: Experiencia Laboral
class ExperienciaLaboralForm(forms.ModelForm):
    class Meta:
        model = ExperienciaLaboral
        fields = ['puesto', 'empresa', 'fecha_inicio', 'fecha_fin', 'descripcion']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

# =========================
# FORMULARIO: Estudio
class EstudioForm(forms.ModelForm):
    class Meta:
        model = Estudio
        fields = ['institucion', 'titulo_obtenido', 'fecha_inicio', 'fecha_fin', 'descripcion']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

# =========================
# FORMULARIO: Hobby
class HobbyForm(forms.ModelForm):
    class Meta:
        model = Hobby
        fields = ['nombre', 'descripcion']

# =========================
# FORMULARIO: Habilidad Técnica
class HabilidadForm(forms.ModelForm):
    class Meta:
        model = Habilidad
        fields = ['nombre', 'nivel']
        widgets = {
            'nivel': forms.Select(attrs={'class': 'form-control'}),
        }

# FORMULARIO: Habilidad Blanda
class HabilidadBlandaForm(forms.ModelForm):
    class Meta:
        model = HabilidadBlanda
        fields = ['nombre', 'icono']
        widgets = {
            'icono': forms.TextInput(attrs={'class': 'form-control'}),
        }
