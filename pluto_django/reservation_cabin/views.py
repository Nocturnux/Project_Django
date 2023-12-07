from django.shortcuts import render, redirect

from reservation_cabin.models import Reservation_cabin

def reservation_cabin(request):    
    reservation_cabin_list = Reservation_cabin.objects.all()    
    return render(request, 'reservation_cabin/index.html', {'reservation_cabin_list': reservation_cabin_list})

def change_status_reservation_cabin(request, reservation_cabin_id):
    reservation_cabin = Reservation_cabin.objects.get(pk=reservation_cabin_id)
    reservation_cabin.status = not reservation_cabin.status
    reservation_cabin.save()
    return redirect('reservation_cabin')