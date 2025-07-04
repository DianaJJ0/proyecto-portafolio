from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(attrs={
            'placeholder': 'Tu nombre completo',
            'class': 'form-control' # Usa la clase que ya tienes estilizada
        }),
        label='Nombre completo'
    )
    correo = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'tu-correo@ejemplo.com',
            'class': 'form-control'
        }),
        label='Correo electrónico'
    )
    asunto = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'placeholder': 'Asunto del mensaje',
            'class': 'form-control'
        }),
        label='Asunto'
    )
    mensaje = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Escribe tu mensaje aquí...',
            'class': 'form-control',
            'rows': 5
        }),
        label='Mensaje'
    )