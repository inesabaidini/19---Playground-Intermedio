from django.urls import path
from curso.views import *

urlpatterns = [
    path('inicio/', inicio, name='coder-inicio'),
    path('cursos/', cursos, name='coder-cursos'),
    path('profesores/', profesores, name='coder-profesores'),
    path('estudiante/', estudiante, name='coder-estudiante'),
    path('entregables/', entregables, name='coder-entregables'),
    path('cursos/crear/', creacion_curso, name='coder-creacion-curso'),
]
