from django.urls import path
from curso.views import *

urlpatterns = [
    path('', inicio),
    path('cursos/', cursos),
    path('profesores/', profesores),
    path('estudiante/', estudiante),
    path('entregables/', entregables),
]
