from django.shortcuts import render
from django.http import HttpResponse
from curso.models import *

# Create your views here.

def inicio(request):
    return render(request, 'curso/base.html')

def cursos(request):
    return render(request, 'curso/cursos.html')

def estudiante(request):
    return render(request, 'curso/estudiante.html')

def profesores(request):
    return render(request, 'curso/profesores.html')

def entregables(request):
    return render(request, 'curso/entregables.html')

