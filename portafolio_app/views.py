from django.shortcuts import render
from .models import Proyecto
from .forms import ContactoForm 

# Create your views here.
def inicio(request):
    return render(request, 'portafolio/inicio.html')

def proyectos(request):
    lista_proyectos = Proyecto.objects.all()
    return render(request, 'portafolio/proyectos.html', {'proyectos': lista_proyectos})

def sobre_mi(request):
    return render(request, 'portafolio/sobre_mi.html')

def contacto(request):
    # Creamos una "instancia" o un objeto de nuestro formulario
    form = ContactoForm() 
    
    # Se lo pasamos a la plantilla en el diccionario de contexto.
    # La clave 'form' es la que usará la plantilla HTML.
    return render(request, 'portafolio/contacto.html', {'form': form})
