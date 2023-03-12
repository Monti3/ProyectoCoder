from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from AppCoder.forms import CursoFormulario, EstudianteFormulario, ProfesorFormulario, EntregableFormulario
from AppCoder.models import Curso, Estudiante, Entregable, Profesor
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView



App_name = 'AppCoder'
# Create your views here.

# funciones de la aplicacion

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


 
def cursoFormulario(request): # funcion para crear un curso
 
    if request.method == "POST": # si se envia un formulario
 
        miFormulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
        if miFormulario.is_valid(): # si el formulario es valido
            informacion = miFormulario.cleaned_data # guardo los datos del formulario en una variable
            curso = Curso(nombre=informacion["curso"], camada=informacion["camada"]) # creo un objeto de tipo Curso y le paso los datos del formulario
            curso.save() # guardo el curso en la base de datos
            return render(request, "inicio.html") # ya completo el formulario, hago un render de la pagina de inicio.html
    else:
        miFormulario = CursoFormulario() # si no se envia un formulario, creo un formulario vacio
 
    return render(request, "cursoFormulario.html", {"miFormulario": miFormulario}) # hago un render de la pagina cursoFormulario.html y le paso el formulario

def profesorFormulario(request): # funcion para crear un profesor
    if request.method == "POST": # si se envia un formulario

        miFormulario = ProfesorFormulario(request.POST) # creo un objeto de tipo ProfesorFormulario y le paso el request

        if miFormulario.is_valid(): # si el formulario es valido

            informacion = miFormulario.cleaned_data # guardo los datos del formulario en una variable
 
            profesor = Profesor(nombre=informacion["nombre"], apellido=informacion["apellido"],  # creo un objeto de tipo Profesor y le paso los datos del formulario
            email=informacion["email"], profesion=informacion["profesion"]) 

            profesor.save()     # guardo el objeto del tipo profesor en la base de datos

            return render(request, "inicio.html") # ya completo el formulario, hago un render de la pagina de inicio.html

    else:
        miFormulario = ProfesorFormulario() # si no se envia un formulario, creo un formulario vacio
        
    return render(request,'profesorFormulario.html', {"miFormulario": miFormulario})

# funcion para crear un -estudiante
def estudianteFormulario(request):
    if request.method == "POST": # si se envia un formulario
        miFormulario = EstudianteFormulario(request.POST) # creo un objeto de tipo EstudianteFormulario y le paso el request
        if miFormulario.is_valid(): # si el formulario es valido
            informacion = miFormulario.cleaned_data # guardo los datos del formulario en una variable
            estudiante = Estudiante(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"]) # creo un objeto de tipo Estudiante y le paso los datos del formulario
            estudiante.save() # guardo el estudiante en la base de datos
            return render(request, "inicio.html") # ya completo el formulario, hago un render de la pagina de inicio.html
    else:
        miFormulario = EstudianteFormulario() # si no se envia un formulario, creo un formulario vacio
    return render(request,'estudianteFormulario.html', {"miFormulario": miFormulario}) # hago un render de la pagina estudianteFormulario.html y le paso el formulario

# funcion para crear un entregable
def entregableFormulario(request):
    # si se envia un formulario
    if request.method == "POST":
        miFormulario = EntregableFormulario(request.POST) # creo un objeto de tipo EntregableFormulario y le paso el request
        if miFormulario.is_valid():  # si el formulario es valido
            informacion = miFormulario.cleaned_data # guardo los datos del formulario en una variable
            entregable = Entregable(nombre=informacion["nombre"], fechaDeEntrega=informacion["fechaDeEntrega"], entregado=informacion["entregado"]) # creo un objeto de tipo Entregable y le paso los datos del formulario
            entregable.save() # guardo el entregable en la base de datos
            return render(request, "inicio.html") # hago un render de la pagina inicio.html
    else:
        miFormulario = EntregableFormulario()
    return render(request,'entregableFormulario.html', {"miFormulario": miFormulario})




def BusquedaCamada(request): # funcion para buscar por camada

    return render(request, 'busquedaCamada.html')

# funcion para buscar por camada
def buscar(request):
    if request.GET['camada']: # si se ingreso una camada
        camada = request.GET['camada'] # guardo la camada en una variable
        cursos = Curso.objects.filter(camada=camada) # busco los cursos con esa camada
        return render(request, 'resultadosBusqueda.html', {'cursos': cursos, 'camada': camada})  # hago un render de la pagina resultadosBusqueda.html y le paso los cursos y la camada
     # si no se ingreso una camada, hago un render de la pagina resultadosBusqueda.html y le paso un mensaje de error
    else:  
        respuesta = 'No ingresaste ninguna camada' 

    return HttpResponse(respuesta)

def leerProfesores(request): # funcion para leer los profesores
    profesores = Profesor.objects.all() # guardo todos los profesores en una variable
    contexto = {'profesores': profesores} # creo un contexto con los profesores
    return render(request, 'leerProfesores.html', contexto) # hago un render de la pagina leerProfesores.html y le paso los profesores

def eliminarProfesor(request, profesor_nombre):
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    profesor.delete()

    profesores = Profesor.objects.all()
    contexto = {"profesores":profesores}
    return render(request, "leerProfesores.html", contexto)

def editarProfesor(request, profesor_nombre):
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            profesor.nombre = informacion['nombre']
            profesor.apellido = informacion['apellido']
            profesor.email = informacion['email']
            profesor.profesion = informacion['profesion']

            profesor.save()
            return render(request, "inicio.html")
    else:
        miFormulario = ProfesorFormulario(initial={'nombre':profesor.nombre, 
                                                   'apellido':profesor.apellido, 
                                                   'email':profesor.email, 
                                                   'profesion':profesor.profesion})
        return render(request, "editarProfesor.html", 
                      {"miFormulario":miFormulario, "profesor_nombre":profesor_nombre})


class CursoList(ListView):
    model = Curso
    template_name = "cursos_list.html"

class CursoDetalle(DetailView):
    model = Curso
    template_name = "curso_detalle.html"

class CursoCreacion(CreateView):
    model = Curso
    template_name = "cursos_form.html"
    success_url = reverse_lazy("AppCoder:List")
    fields = ['nombre', 'camada']

class CursoUpdate(UpdateView):
    model = Curso
    success_url = "/AppCoder/curso/list"
    template_name = "cursos_form.html"
    fields = ['nombre', 'camada']

class CursoDelete(DeleteView):
    model = Curso
    template_name = "curso_confirm_delete.html"
    success_url = "/AppCoder/curso/list"