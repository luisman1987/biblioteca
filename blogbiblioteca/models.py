from django.db import models
from django.contrib import admin

class Libro(models.Model):
    ISBN = models.CharField(max_length=13)
    titulo = models.CharField(max_length=20)
    #imagen=models.FileField(null=True,blank=True)
    autor = models.CharField(max_length=20)
    editorial = models.CharField(max_length=20)
    pais = models.CharField(max_length=20)
    ano = models.CharField(max_length=4)


    def __str__(self):              # __unicode__ on Python 2
        return self.ISBN

class Persona(models.Model):
    dpi = models.CharField(max_length=13)
    nombre = models.CharField(max_length=30)
    def __str__(self):              # __unicode__ on Python 2
        return self.dpi


class Prestamo(models.Model):
    fechaprestamo = models.DateField()
    fechadevolucionp = models.DateField()
    fechadevolucionr = models.DateField()
    libro = models.ManyToManyField(Libro)
    persona = models.ForeignKey(Persona)

class PrestamoInLine(admin.TabularInline):
    model = Prestamo
    extra = 1

class PrestamoAdmin(admin.ModelAdmin):
    inlines = (PrestamoInLine,)
