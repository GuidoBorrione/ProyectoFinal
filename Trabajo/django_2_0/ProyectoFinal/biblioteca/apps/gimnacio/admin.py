from django.contrib import admin

# Register your models here.

from .models import Aparato, Clase, Clases_Socios, Entrenador, Actividad, Entrenador_Actividad, Sala, Socio

admin.site.register(Aparato)
admin.site.register(Clase)
admin.site.register(Entrenador)
admin.site.register(Actividad)
admin.site.register(Sala)
admin.site.register(Socio)
admin.site.register(Clases_Socios)
admin.site.register(Entrenador_Actividad)