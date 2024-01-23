from django.shortcuts import render,redirect

# Create your views here.

from services.models import Services

def services (request):    
    services_list = Services.objects.all()    
    return render(request, 'services/index.html', {'services_list': services_list})

def change_status_services(request, services_id):
    services = Services.objects.get(pk=services_id)
    services.status = services.status
    services.save()
    return redirect('services')

from .forms import ServicesForm

def create_services(request):
    form = ServicesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('services')    
    return render(request, 'services/create.html', {'form': form})