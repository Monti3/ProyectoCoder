from django.urls import path
from AppCoder import views

# acá se definen las rutas de la aplicacion
urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('cursos/', views.cursos, name="Cursos"),
    path('estudiantes/', views.estudiantes, name="Estudiantes"),
    path('entregables/', views.entregables , name="Entregables"),
    path('profesores/', views.Profesores, name="Profesores"),
    path('cursoFormulario/', views.cursoFormulario, name="CursoFormulario"),
    path('profesorFormulario/', views.profesorFormulario, name="ProfesorFormulario"),
    path('estudianteFormulario/', views.estudianteFormulario, name="EstudianteFormulario"),
    path('entregableFormulario/', views.entregableFormulario, name="EntregableFormulario"),
    path('busquedaCamada/', views.BusquedaCamada, name="BusquedaCamada"),
    path('buscar/', views.buscar),
    
    
]