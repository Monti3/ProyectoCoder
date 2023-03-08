from django.contrib import admin
from .models import Curso, Estudiante, Entregable, Profesor
# Register your models here.
# registro de los modelos en el admin
admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Entregable)
admin.site.register(Profesor)
