from django import forms
from . models import TypeCabin

class TypeCabinForm(forms.ModelForm):
    class Meta:
        model = TypeCabin
        fields = "__all__"
        exclude = ['status']
        labels = {
            'name': 'Nombre',
                                
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ingresa el nombre'}),           
        }