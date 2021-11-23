from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

# Create your models here.

class Aparato(models.Model):
    Codigo_Aparato = models.AutoField(primary_key=True)
    Descripción = models.TextField(blank=False, null=False)
    Estado = models.CharField(max_length=200, blank=False, null=False)

    class Meta:
        verbose_name= 'Aparato'
        verbose_name_plural= 'Aparatos'
        ordering = ['Estado']    
    
    def __str__(self):
        return self.Estado

class Clase(models.Model):
    Codigo_Clase = models.AutoField(primary_key=True)
    Horario = models.CharField(max_length=200, blank=False, null=False)
    Día = models.CharField(max_length=200, blank=False, null=False)

    class Meta:
        verbose_name= 'Clase'
        verbose_name_plural= 'Clases'
        ordering = ['Día']    
    
    def __str__(self):
        return self.Día

class Entrenador(models.Model):
    DNI_E = models.CharField(primary_key=True, max_length=25)
    Nombre = models.CharField(max_length=200, blank=False, null=False)
    Apellido = models.CharField(max_length=200, blank=False, null=False)
    Titulación = models.CharField(max_length=200, blank=False, null=False)
    Experiencia_Profesional = models.CharField(max_length=200, blank=False, null=False)
    Telefono = models.CharField(max_length=200, blank=False, null=False)
    Codigo_Clase = models.ForeignKey(Clase, on_delete=models.CASCADE)

    class Meta:
        verbose_name= 'Entrenador'
        verbose_name_plural= 'Entrenadores'
        ordering = ['Apellido']    
    
    def __str__(self):
        return self.Apellido

class Actividad(models.Model):
    ID_Actividad = models.AutoField(primary_key=True)
    Descripción = models.TextField(blank=False, null=False)
    Codigo_Clase = models.ForeignKey(Clase, on_delete=models.CASCADE)

    class Meta:
        verbose_name= 'Actividad'
        verbose_name_plural= 'Actividades'
        ordering = ['Descripción']    
    
    def __str__(self):
        return self.Descripción

class Sala(models.Model):
    NumerodeSala = models.AutoField(primary_key=True)
    Tipo =  models.CharField(max_length=200, blank=False, null=False)
    Ubicación = models.CharField(max_length=200, blank=False, null=False)
    Metros_Cuadrados = models.CharField(max_length=25, blank=False, null=False)
    Codigo_Aparato = models.ForeignKey(Aparato, on_delete=models.CASCADE)
    Codigo_Clase = models.ForeignKey(Clase, on_delete=models.CASCADE)

    class Meta:
        verbose_name= 'Sala'
        verbose_name_plural= 'Salas'
        ordering = ['Metros_Cuadrados']    
    
    def __str__(self):
        return self.Metros_Cuadrados

class Socio(models.Model):
    DNI_S = models.CharField(max_length=20, blank=False, null=False)
    Nombre = models.CharField(max_length=200, blank=False, null=False)
    Apellido = models.CharField(max_length=200, blank=False, null=False)
    Dirección = models.CharField(max_length=200, blank=False, null=False)
    Profesión = models.CharField(max_length=200, blank=False, null=False)
    CBU = models.CharField(max_length=25, blank=False, null=False)
    Telefono = models.CharField(max_length=25, blank=False, null=False)

    class Meta:
        verbose_name= 'Socio'
        verbose_name_plural= 'Socios'
        ordering = ['Apellido']    
    
    def __str__(self):
        return self.Apellido

class Clases_Socios(models.Model):
    Codigo_Clase = models.ForeignKey(Clase, on_delete=models.CASCADE)
    DNI_S = models.ForeignKey(Socio, on_delete=models.CASCADE)
    Descripción = models.TextField(blank=False, null=False)

    class Meta:
        verbose_name= 'Socio-Actividad'
        verbose_name_plural= 'Socios Actividades'
        ordering = ['Descripción']    
    
    def __str__(self):
        return self.Descripción


class Entrenador_Actividad(models.Model):
    DNI_E = models.ForeignKey(Entrenador, on_delete=models.CASCADE)
    ID_Actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    Descripción = models.TextField(blank=False, null=False)

    class Meta:
        verbose_name= 'Entrenador-Actividad'
        verbose_name_plural= 'Entrenadores-Actividades'
        ordering = ['Descripción']    
    
    def __str__(self):
        return self.Descripción


