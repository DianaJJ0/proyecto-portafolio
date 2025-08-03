from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Proyecto, ExperienciaLaboral, Estudio, Hobby, Habilidad, HabilidadBlanda, Contacto
from .forms import HabilidadBlandaForm, HabilidadForm, ProyectoForm, ExperienciaLaboralForm, EstudioForm, HobbyForm, ContactoForm

# =========================
# VISTA: Login
def login_view(request):
    """
    Vista para iniciar sesión.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('sobre_mi')
        else:
            return render(request, 'portafolio/login.html', {'error': 'Usuario o contraseña incorrectos'})
    return render(request, 'portafolio/login.html')


# =========================
# VISTA: Logout
def logout_view(request):
    """
    Vista para cerrar sesión.
    """
    logout(request)
    return redirect('login')


# =========================
# VISTA: Sobre mí (pública)
def sobre_mi(request):
    habilidades_tecnicas = Habilidad.objects.all()
    habilidades_blandas = HabilidadBlanda.objects.all()
    return render(request, 'portafolio/sobre_mi.html', {
        'habilidades_tecnicas': habilidades_tecnicas,
        'habilidades_blandas': habilidades_blandas,
    })

# =========================
# VISTA: Contacto
def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Tu mensaje ha sido enviado exitosamente!")
            return redirect('contacto')
    else:
        form = ContactoForm()
    return render(request, 'portafolio/contacto.html', {'form': form})


# ===============================================================================================
# CRUD: PROTEGER LAS VISTAS CRUD CON @login_required para que solo usuarios autenticados
# puedan acceder a ellas y modificarlas, y redirigir a la página de inicio de sesión si no están autenticados.
# ===============================================================================================

# =========================
# VISTAS CRUD: Proyectos

# listar proyectos
def lista_proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'portafolio/lista_proyectos.html', {'proyectos': proyectos})

# crear proyecto
@login_required
def crear_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listaProyectos')
    else:
        form = ProyectoForm()
    return render(request, 'portafolio/formulario.html', {'form': form})

# editar proyecto
@login_required
def editar_proyecto(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    form = ProyectoForm(request.POST or None, instance=proyecto)
    if form.is_valid():
        form.save()
        return redirect('listaProyectos')
    return render(request, 'portafolio/formulario.html', {'form': form})

# eliminar proyecto
@login_required
def eliminar_proyecto(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    if request.method == 'POST':
        proyecto.delete()
        return redirect('listaProyectos')
    return render(request, 'portafolio/confirmar_eliminar.html', {'objeto': proyecto, 'tipo': 'proyecto'})



# =========================
# VISTAS CRUD: Experiencia Laboral

# listar experiencia laboral
def lista_experiencia(request):
    experiencia = ExperienciaLaboral.objects.all()
    return render(request, 'portafolio/lista_experiencia.html', {'experiencia': experiencia})

# crear experiencia
@login_required
def crear_experiencia(request):
    if request.method == 'POST':
        form = ExperienciaLaboralForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_experiencia')
    else:
        form = ExperienciaLaboralForm()
    return render(request, 'portafolio/formulario_experiencia.html', {'form': form})

# editar experiencia
@login_required
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

# eliminar experiencia
@login_required
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
# VISTA: Proyectos destacados
@login_required
def proyectos_destacados(request):
    """
    Muestra la página de proyectos destacados.
    """
    proyectos = Proyecto.objects.all()
    return render(request, 'portafolio/proyectos.html', {'proyectos': proyectos})


# =========================
# VISTAS CRUD: Estudios

# listar estudios
def lista_estudios(request):
    """
    Lista todos los estudios registrados.
    """
    estudios = Estudio.objects.all()
    return render(request, 'portafolio/lista_estudios.html', {'estudios': estudios})

# crear estudio
@login_required
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

# editar estudio
@login_required
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

# eliminar estudio
@login_required
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

# listar hobbies
def lista_hobbies(request):
    """
    Lista todos los hobbies registrados.
    """
    hobbies = Hobby.objects.all()
    return render(request, 'portafolio/lista_hobbies.html', {'hobbies': hobbies})

# crear hobby
@login_required
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

# editar hobby
@login_required
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

# eliminar hobby
@login_required
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
# VISTAS CRUD: Habilidad Técnica

# listar habilidades técnicas
def lista_habilidades(request):
    habilidades = Habilidad.objects.all()
    return render(request, 'portafolio/lista_habilidades.html', {'habilidades': habilidades})

# Crear habilidad técnica
@login_required
def crear_habilidad(request):
    if request.method == 'POST':
        form = HabilidadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_habilidades')
    else:
        form = HabilidadForm()
    return render(request, 'portafolio/formulario_habilidad.html', {'form': form})

# Editar habilidad técnica
@login_required
def editar_habilidad(request, pk):
    habilidad = get_object_or_404(Habilidad, pk=pk)
    form = HabilidadForm(request.POST or None, instance=habilidad)
    if form.is_valid():
        form.save()
        return redirect('lista_habilidades')
    return render(request, 'portafolio/formulario_habilidad.html', {'form': form})

# Eliminar habilidad técnica
@login_required
def eliminar_habilidad(request, pk):
    habilidad = get_object_or_404(Habilidad, pk=pk)
    if request.method == 'POST':
        habilidad.delete()
        return redirect('lista_habilidades')
    return render(request, 'portafolio/confirmar_eliminar.html', {'objeto': habilidad, 'tipo': 'habilidad'})


# =========================
# VISTAS CRUD: Habilidad Blanda

# listar habilidades blandas
def lista_habilidades_blandas(request):
    habilidades_blandas = HabilidadBlanda.objects.all()
    return render(request, 'portafolio/lista_habilidades_blandas.html', {'habilidades_blandas': habilidades_blandas})

# Crear habilidad blanda
@login_required
def crear_habilidad_blanda(request):
    if request.method == 'POST':
        form = HabilidadBlandaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_habilidades_blandas')
    else:
        form = HabilidadBlandaForm()
    return render(request, 'portafolio/formulario_habilidad_blanda.html', {'form': form})

# Editar habilidad blanda
@login_required
def editar_habilidad_blanda(request, pk):
    habilidad_blanda = get_object_or_404(HabilidadBlanda, pk=pk)
    form = HabilidadBlandaForm(request.POST or None, instance=habilidad_blanda)
    if form.is_valid():
        form.save()
        return redirect('lista_habilidades_blandas')
    return render(request, 'portafolio/formulario_habilidad_blanda.html', {'form': form})

# Eliminar habilidad blanda
@login_required
def eliminar_habilidad_blanda(request, pk):
    habilidad_blanda = get_object_or_404(HabilidadBlanda, pk=pk)
    if request.method == 'POST':
        habilidad_blanda.delete()
        return redirect('lista_habilidades_blandas')
    return render(request, 'portafolio/confirmar_eliminar.html', {'objeto': habilidad_blanda, 'tipo': 'habilidad blanda'})
