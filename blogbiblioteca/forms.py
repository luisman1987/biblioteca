from django import forms
from blogbiblioteca.models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ('ISBN', 'titulo','autor','editorial','pais','ano')
