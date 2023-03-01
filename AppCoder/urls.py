from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio),
    path('cursos/', views.cursos),
    path('estudiantes/', views.estudiantes),
    path('entregables/', views.entregables),
    path('profesores/', views.Profesores),
    
    
]