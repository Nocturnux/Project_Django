from django import forms
from . models import Cabin

class CabinForm(forms.ModelForm):
    class Meta:
        model = Cabin
        fields = "__all__"
        exclude = ['status']
        labels = {
            'name': 'Nombre',
            'capacity': 'Capacidad',
            'typeCabin': 'Tipo cabaña',
            'description': 'Descripción',                        
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ingresa el nombre'}),
            'capacity': forms.TextInput(attrs={'placeholder': 'Ingresa la capacidad'}),
            'typeCabin': forms.TextInput(attrs={'placeholder': 'Ingresa el tipo de cabaña'}),
            'description': forms.TextInput(attrs={'placeholder': 'Ingresa la descripción'}),
            }