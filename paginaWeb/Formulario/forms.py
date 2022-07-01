from django import forms
from .models import Formulario
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

class FormularioForm(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = ['nombre', 'correo', 'asunto','mensaje']
 
        labels = {
            'nombre': 'Nombre',
            'correo': 'Correo',
            'asunto': 'Asunto',
            'mensaje':'Mensaje',
 
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'asunto': forms.TextInput(attrs={'class': 'form-control'}),
            'mensaje': forms.TextInput(attrs={'class': 'form-control'}),
        }
