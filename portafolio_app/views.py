from django.shortcuts import render, redirect, get_object_or_404
from .models import Proyecto
from .forms import ProyectoForm 



# Create your views here.
"""def inicio(request):
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
    return render(request, 'portafolio/contacto.html', {'form': form}) """

#Leer listar todos los proyectos
def listaProyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'portfolio/proyectos.html', {'proyectos': proyectos})

#Crear un nuevo proyecto
def crearProyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listaProyectos')
    else:
        form = ProyectoForm()
    return render(request, 'portfolio/formulario.html', {'form': form})

#Actualizar proyecto
def editarProyecto(request,pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    form = ProyectoForm(request.POST or None, instance=proyecto)
    if form.is_valid():
        form.save()
        return redirect('listaProyectos')
    return render(request, 'portfolio/formulario.html', {'form': form})

#Eliminar proyecto
def eliminarProyecto(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    if request.method == 'POST':
        proyecto.delete()
        return redirect('listaProyectos')
    return render(request, 'portfolio/confirmar_eliminar.html', {'proyecto': proyecto})




