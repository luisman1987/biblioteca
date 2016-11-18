from django.contrib import admin
from blogbiblioteca.models import Libro,Persona,Prestamo

admin.site.register(Persona)
admin.site.register(Libro)
admin.site.register(Prestamo)
