
from django.shortcuts import render, redirect

from typeCabin.models import TypeCabin

def typeCabin(request):    
    typeCabin_list = TypeCabin.objects.all()    
    return render(request, 'typeCabin/index.html', {'typeCabin_list': typeCabin_list})

def change_status_typeCabin(request, typeCabin_id):
    typeCabin = typeCabin.objects.get(pk=typeCabin_id)
    typeCabin.status = not typeCabin.status
    typeCabin.save()
    return redirect('typeCabin')