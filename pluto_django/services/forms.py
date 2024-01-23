from django import forms
from . models import Services

class ServicesForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = "__all__"
        exclude = ['status']
        labels = {
            'name': 'Nombre',
            'value': 'Valor',                   
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ingresa el nombre'}),
            'value': forms.TextInput(attrs={'placeholder': 'Ingresa el valor'}),          
        }