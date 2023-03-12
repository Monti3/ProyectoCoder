from django.urls import path
from AppCoder import views

app_name = 'AppCoder'
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
    path('leerProfesores/', views.leerProfesores, name='LeerProfesores'),
    path('eliminarProfesor/<profesor_nombre>/',views.eliminarProfesor, name="EliminarProfesor"),
    path('editarProfesor/<profesor_nombre>', views.editarProfesor, name='EditarProfesor'),
    path('curso/list', views.CursoList.as_view(), name='List'),
    path('<int:pk>', views.CursoDetalle.as_view(), name='Detail'),
    path('nuevo', views.CursoCreacion.as_view(), name='New'),
    path('editar/<int:pk>', views.CursoUpdate.as_view(), name='Edit'),
    path('borrar/<int:pk>', views.CursoDelete.as_view(), name='Delete'),
]