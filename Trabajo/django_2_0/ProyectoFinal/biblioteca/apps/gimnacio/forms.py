from django import forms


from .models import Actividad, Aparato, Clase, Clases_Socios, Entrenador, Entrenador_Actividad, Sala, Socio

class AparatoForm(forms.ModelForm):

    class Meta:
        model = Aparato
        fields = ['Estado', 'Descripción',]
        
class ClaseForm(forms.ModelForm):

    class Meta:
        model = Clase
        fields = ['Día', 'Horario',]


class EntrenadorForm(forms.ModelForm):

    class Meta:
        model = Entrenador
        fields = ['DNI_E', 'Nombre', 'Apellido', 'Titulación','Experiencia_Profesional', 'Telefono', 'Codigo_Clase',]


class ActividadForm(forms.ModelForm):

    class Meta:
        model = Actividad
        fields = ['Descripción', 'Codigo_Clase',]


class SalaForm(forms.ModelForm):

    class Meta:
        model = Sala
        fields = ['Metros_Cuadrados', 'Ubicación', 'Tipo','Codigo_Aparato', 'Codigo_Clase',]


class SocioForm(forms.ModelForm):

    class Meta:
        model = Socio
        fields = ['DNI_S', 'Nombre', 'Apellido', 'Dirección','Profesión','CBU','Telefono',]



class Clase_SocioForm(forms.ModelForm):

    class Meta:
        model = Clases_Socios
        fields = ['DNI_S','Codigo_Clase','Descripción',]



class Entrenador_ActividadForm(forms.ModelForm):

    class Meta:
        model = Entrenador_Actividad
        fields = ['DNI_E', 'ID_Actividad', 'Descripción',]