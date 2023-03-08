from django import forms
 
 # formularios de la aplicacion
 
class CursoFormulario(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()

class EstudianteFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()

class ProfesorFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    profesion = forms.CharField()

class EntregableFormulario(forms.Form):
    nombre = forms.CharField()
    fechaDeEntrega = forms.DateField()
    entregado = forms.BooleanField()

