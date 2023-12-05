from django.shortcuts import render, redirect

from reservation_services.models import Reservation_service

def reservation_services(request):    
    reservation_services_list = Reservation_service.objects.all()    
    return render(request, 'reservation_services/index.html', {'reservation_services_list': reservation_services_list})

def change_status_reservation_service(request, reservation_service_id):
    reservation_service = Reservation_service.objects.get(pk=reservation_service_id)
    reservation_service.status = not reservation_service.status
    reservation_service.save()
    return redirect('reservation_services')