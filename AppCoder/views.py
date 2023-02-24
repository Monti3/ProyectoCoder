from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso

# Create your views here.

def curso(self):
    curso = Curso(nombre="HTML", camada=1234)
    curso.save()

    texto = "Curso: " + curso.nombre + " Camada: " + str(curso.camada)
    return HttpResponse(texto)