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

def creacion_curso(request):
    if request == "POST":
        nombre_curso = request.POST['curso']
        numero_camada = int(request.POST['camada'])
        print(numero_camada, type(numero_camada))
        curso = Curso(nombre=nombre_curso, camada=numero_camada)
        curso.save()
    return render(request, 'curso/curso_formulario.html')
