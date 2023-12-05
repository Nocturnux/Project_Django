from django.shortcuts import render, redirect

from qualification.models import Qualification

def qualification(request):    
    qualification_list = Qualification.objects.all()    
    return render(request, 'qualification/index.html', {'qualification_list': qualification_list})

def change_status_qualification(request, qualification_id):
    qualification = Qualification.objects.get(pk=qualification_id)
    qualification.status = not qualification.status
    qualification.save()
    return redirect('qualification')