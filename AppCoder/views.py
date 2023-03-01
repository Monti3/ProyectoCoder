from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def cursos(request):
    return render(request, 'cursos.html')

def inicio(request):
    return render(request,'inicio.html')

def estudiantes(request):
    return render(request,'estudiantes.html')

def entregables(request):
    return render(request,'entregables.html')

def Profesores(request):
    return render(request,'Profesores.html')