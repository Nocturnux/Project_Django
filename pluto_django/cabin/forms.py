from django import forms
from . models import Cabin

class CabinForm(forms.ModelForm):
    class Meta:
        model = Cabin
        fields = "__all__"
        exclude = ['status']
        labels = {
            'image': 'Imagen',
            'name': 'Nombre',
            'capacity': 'Capacidad',
            'typeCabin': 'Tipo cabaña',
            'description': 'Descripción',  
            'value': 'valor',                      
        }
        widgets = {
            'image': forms.FileInput(attrs={'placeholder': 'Ingrese la imagen de la cabaña'}),
            'name': forms.TextInput(attrs={'placeholder': 'Ingresa el nombre'}),
            'capacity': forms.TextInput(attrs={'placeholder': 'Ingresa la capacidad'}),
            'typeCabin': forms.TextInput(attrs={'placeholder': 'Ingresa el tipo de cabaña'}),
            'description': forms.TextInput(attrs={'placeholder': 'Ingresa la descripción'}),
            'value': forms.TextInput(attrs={'placeholder': 'Ingresa el valor'}),
            }