from django.shortcuts import render
from django.http import HttpResponse
from curso.models import *

# Create your views here.

def inicio(request):
    return render(request, 'curso/index.html')

def cursos(request):
    return HttpResponse('Bienvenidx /n Estás en cursos')

def estudiante(request):
    return HttpResponse('Bienvenidx /n Estás en alumnos')

def profesores(request):
    return HttpResponse('Bienvenidx /n Estás en profesores')

def entregables(request):
    return HttpResponse('Bienvenidx /n Estás en entregables')

