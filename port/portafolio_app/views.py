from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'portafolio/inicio.html')

def proyectos(request):
    return render(request, 'portafolio/proyectos.html')

def sobre_mi(request):
    return render(request, 'portafolio/sobre_mi.html')

def contacto(request):
    return render(request, 'portafolio/contacto.html')
