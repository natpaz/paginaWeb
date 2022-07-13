from .models import Producto
from django import forms
 
class ProductoForm(forms.ModelForm):
    
 
    class Meta:
        model = Producto
        fields = (
            'codigo',
            'nombre',
            'precio',
            'imagen'
        )
        labels = {
            'codigo':'Codigo',
            'nombre':'Nombre',
            'precio':'Precio',
            'imagen':'Imagen'
        }
        widgets = {
            'codigo':forms.TextInput(attrs={'class':'form-control'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'precio':forms.TextInput(attrs={'class':'form-control'}),
            #'imagen':forms.FileInput(attrs={'class':'form-control','type':'file'}),
        }
 
