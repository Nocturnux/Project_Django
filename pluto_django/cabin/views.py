from django.shortcuts import render,redirect

# Create your views here.
from cabin.models import Cabin

def cabin(request):    
    cabin_list = Cabin.objects.all()    
    return render(request, 'cabin/index.html', {'cabin_list': cabin_list})

def change_status_cabin(request, cabin_id):
    cabin= Cabin.objects.get(pk=cabin_id)
    cabin.status = not cabin.status
    cabin.save()
    return redirect('cabin')

from .forms import CabinForm

def create_cabin(request):
    form = CabinForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('cabin')    
    return render(request, 'cabin/create.html', {'form': form})