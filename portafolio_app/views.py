from django.shortcuts import render, redirect, get_object_or_404
from .models import Proyecto, ExperienciaLaboral, Estudio, Hobby
from .forms import ProyectoForm, ExperienciaLaboralForm, EstudioForm, HobbyForm, ContactoForm

# =========================
# VISTA: Página de inicio
# =========================
def inicio(request):
    return render(request, 'portafolio/inicio.html')

def sobre_mi(request):
    return render(request, 'portafolio/sobre_mi.html')

def contacto(request):
    """
    Vista para la página de contacto.
    Renderiza la plantilla contacto.html con el formulario de contacto.
    """
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            # Aquí puedes procesar el formulario (enviar email, guardar en BD, etc)
            # Por ahora solo puedes mostrar un mensaje o redirigir
            # return redirect('inicio')  # Ejemplo: redirigir al inicio después de enviar
            pass
    else:
        form = ContactoForm()
    return render(request, 'portafolio/contacto.html', {'form': form})
# =========================
# VISTAS CRUD: Proyecto
# =========================
def listaProyectos(request):
    """
    Lista todos los proyectos registrados en el portafolio.
    """
    proyectos = Proyecto.objects.all()
    return render(request, 'portafolio/lista_proyectos.html', {'proyectos': proyectos})

def crear_proyecto(request):
    """
    Formulario para crear un nuevo proyecto.
    """
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listaProyectos')
    else:
        form = ProyectoForm()
    return render(request, 'portafolio/formulario.html', {'form': form})

def editar_proyecto(request, pk):
    """
    Formulario para editar un proyecto existente.
    """
    proyecto = get_object_or_404(Proyecto, pk=pk)
    form = ProyectoForm(request.POST or None, instance=proyecto)
    if form.is_valid():
        form.save()
        return redirect('listaProyectos')
    return render(request, 'portafolio/formulario.html', {'form': form})

def eliminar_proyecto(request, pk):
    """
    Vista para confirmar y eliminar un proyecto.
    """
    proyecto = get_object_or_404(Proyecto, pk=pk)
    if request.method == 'POST':
        proyecto.delete()
        return redirect('listaProyectos')
    return render(request, 'portafolio/confirmar_eliminar.html', {'objeto': proyecto, 'tipo': 'proyecto'})

# =========================
# VISTAS CRUD: Experiencia Laboral
# =========================
def lista_experiencia(request):
    """
    Lista todas las experiencias laborales registradas.
    """
    experiencia = ExperienciaLaboral.objects.all()
    return render(request, 'portafolio/lista_experiencia.html', {'experiencia': experiencia})

def crear_experiencia(request):
    """
    Formulario para agregar una nueva experiencia laboral.
    """
    if request.method == 'POST':
        form = ExperienciaLaboralForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_experiencia')
    else:
        form = ExperienciaLaboralForm()
    return render(request, 'portafolio/formulario_experiencia.html', {'form': form})

def editar_experiencia(request, pk):
    """
    Formulario para editar una experiencia laboral existente.
    """
    exp = get_object_or_404(ExperienciaLaboral, pk=pk)
    form = ExperienciaLaboralForm(request.POST or None, instance=exp)
    if form.is_valid():
        form.save()
        return redirect('lista_experiencia')
    return render(request, 'portafolio/formulario_experiencia.html', {'form': form})

def eliminar_experiencia(request, pk):
    """
    Vista para confirmar y eliminar una experiencia laboral.
    """
    exp = get_object_or_404(ExperienciaLaboral, pk=pk)
    if request.method == 'POST':
        exp.delete()
        return redirect('lista_experiencia')
    return render(request, 'portafolio/confirmar_eliminar.html', {'objeto': exp, 'tipo': 'experiencia'})

# =========================
# VISTAS CRUD: Estudios
# =========================
def lista_estudios(request):
    """
    Lista todos los estudios registrados.
    """
    estudios = Estudio.objects.all()
    return render(request, 'portafolio/lista_estudios.html', {'estudios': estudios})

def crear_estudio(request):
    """
    Formulario para agregar un nuevo estudio.
    """
    if request.method == 'POST':
        form = EstudioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_estudios')
    else:
        form = EstudioForm()
    return render(request, 'portafolio/formulario_estudio.html', {'form': form})

def editar_estudio(request, pk):
    """
    Formulario para editar un estudio existente.
    """
    estudio = get_object_or_404(Estudio, pk=pk)
    form = EstudioForm(request.POST or None, instance=estudio)
    if form.is_valid():
        form.save()
        return redirect('lista_estudios')
    return render(request, 'portafolio/formulario_estudio.html', {'form': form})

def eliminar_estudio(request, pk):
    """
    Vista para confirmar y eliminar un estudio.
    """
    estudio = get_object_or_404(Estudio, pk=pk)
    if request.method == 'POST':
        estudio.delete()
        return redirect('lista_estudios')
    return render(request, 'portafolio/confirmar_eliminar.html', {'objeto': estudio, 'tipo': 'estudio'})

# =========================
# VISTAS CRUD: Hobbies
# =========================
def lista_hobbies(request):
    """
    Lista todos los hobbies registrados.
    """
    hobbies = Hobby.objects.all()
    return render(request, 'portafolio/lista_hobbies.html', {'hobbies': hobbies})

def crear_hobby(request):
    """
    Formulario para agregar un nuevo hobby.
    """
    if request.method == 'POST':
        form = HobbyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_hobbies')
    else:
        form = HobbyForm()
    return render(request, 'portafolio/formulario_hobby.html', {'form': form})

def editar_hobby(request, pk):
    """
    Formulario para editar un hobby existente.
    """
    hobby = get_object_or_404(Hobby, pk=pk)
    form = HobbyForm(request.POST or None, instance=hobby)
    if form.is_valid():
        form.save()
        return redirect('lista_hobbies')
    return render(request, 'portafolio/formulario_hobby.html', {'form': form})

def eliminar_hobby(request, pk):
    """
    Vista para confirmar y eliminar un hobby.
    """
    hobby = get_object_or_404(Hobby, pk=pk)
    if request.method == 'POST':
        hobby.delete()
        return redirect('lista_hobbies')
    return render(request, 'portafolio/confirmar_eliminar.html', {'objeto': hobby, 'tipo': 'hobby'})


# =========================
# VISTA: Proyectos destacados
def proyectos_destacados(request):
    """
    Muestra la página de proyectos destacados.
    """
    proyectos = Proyecto.objects.all()
    return render(request, 'portafolio/proyectos.html', {'proyectos': proyectos})