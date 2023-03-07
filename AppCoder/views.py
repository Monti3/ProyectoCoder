from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from AppCoder.forms import CursoFormulario, EstudianteFormulario, ProfesorFormulario, EntregableFormulario
from AppCoder.models import Curso, Estudiante, Entregable, Profesor
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


 
def cursoFormulario(request):
 
    if request.method == "POST":
 
        miFormulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            print(informacion)
            curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
            curso.save()
            return render(request, "inicio.html")
    else:
        miFormulario = CursoFormulario()
 
    return render(request, "cursoFormulario.html", {"miFormulario": miFormulario})

def profesorFormulario(request):
    if request.method == "POST":

        miFormulario = ProfesorFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            profesor = Profesor(nombre=informacion["nombre"], apellido=informacion["apellido"], 
            email=informacion["email"], profesion=informacion["profesion"])

            profesor.save()

            return render(request, "inicio.html")

    else:
        miFormulario = ProfesorFormulario()
        
    return render(request,'profesorFormulario.html', {"miFormulario": miFormulario})

def estudianteFormulario(request):
    if request.method == "POST":
        miFormulario = EstudianteFormulario(request.POST)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            estudiante = Estudiante(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"])
            estudiante.save()
            return render(request, "inicio.html")
    else:
        miFormulario = EstudianteFormulario()
    return render(request,'estudianteFormulario.html', {"miFormulario": miFormulario})

def entregableFormulario(request):
    if request.method == "POST":
        miFormulario = EntregableFormulario(request.POST)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            entregable = Entregable(nombre=informacion["nombre"], fechaDeEntrega=informacion["fechaDeEntrega"], entregado=informacion["entregado"])
            entregable.save()
            return render(request, "inicio.html")
    else:
        miFormulario = EntregableFormulario()
    return render(request,'entregableFormulario.html', {"miFormulario": miFormulario})




def BusquedaCamada(request):

    return render(request, 'busquedaCamada.html')

def buscar(request):
    if request.GET['camada']:
        camada = request.GET['camada']
        cursos = Curso.objects.filter(camada=camada)
        return render(request, 'resultadosBusqueda.html', {'cursos': cursos, 'camada': camada})       
    else:
        respuesta = 'No ingresaste ninguna camada'

    return HttpResponse(respuesta)