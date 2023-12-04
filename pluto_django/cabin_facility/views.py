from django.shortcuts import render, redirect

from cabin_facility.models import Cabin_facility

def cabin_facility(request):    
    cabin_facility_list = Cabin_facility.objects.all()    
    return render(request, 'cabin_facility/index.html', {'cabin_facility_list': cabin_facility_list})

def change_status_cabin_facility(request, cabin_facility_id):
    cabin_facility = Cabin_facility.objects.get(pk=cabin_facility_id)
    cabin_facility.status = not cabin_facility.status
    cabin_facility.save()
    return redirect('cabin_facility')

# Create your views here.
