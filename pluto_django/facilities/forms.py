from django import forms
from . models import Facilities

class FacilitiesForm(forms.ModelForm):
    class Meta:
        model = Facilities
        fields = "__all__"
        exclude = ['status']
        labels = {
            'name': 'Nombre',
                              
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ingresa la comodidad'}),
                   
        }