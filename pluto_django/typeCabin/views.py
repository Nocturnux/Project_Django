
from django.shortcuts import render, redirect

from typeCabin.models import TypeCabin

def typeCabin(request):    
    typeCabin_list = TypeCabin.objects.all()    
    return render(request, 'typeCabin/index.html', {'typeCabin_list': typeCabin_list})

def change_status_typeCabin(request, typeCabin_id):
    typeCabin = TypeCabin.objects.get(pk=typeCabin_id)
    typeCabin.status = not typeCabin.status
    typeCabin.save()
    return redirect('typeCabin')

from .forms import TypeCabinForm

def create_typeCabin(request):
    form = TypeCabinForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('typeCabin')    
    return render(request, 'typeCabin/create.html', {'form': form})