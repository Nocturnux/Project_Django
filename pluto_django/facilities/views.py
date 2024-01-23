
from django.shortcuts import render, redirect

from facilities.models import Facilities

def facilities(request):    
    facilities_list = Facilities.objects.all()    
    return render(request, 'facilities/index.html', {'facilities_list': facilities_list})

def change_status_facilities(request, facilities_id):
    facilities = Facilities.objects.get(pk=facilities_id)
    facilities.status = not facilities.status
    facilities.save()
    return redirect('facilities')

from .forms import FacilitiesForm

def create_facilities(request):
    form = FacilitiesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('facilities')    
    return render(request, 'facilities/create.html', {'form': form})