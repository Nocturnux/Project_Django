from django.shortcuts import render,redirect

# Create your views here.

from reservation_sale.models import Reservation_sale

def reservation_sale(request):    
    reservation_sale_list = Reservation_sale.objects.all()    
    return render(request, 'reservation_sale/index.html', {'reservation_sale_list': reservation_sale_list})

def change_status_reservation_sale(request, reservation_sale_id):
    reservation_sale= Reservation_sale.objects.get(pk=reservation_sale_id)
    reservation_sale.status = not reservation_sale.status
    reservation_sale.save()
    return redirect('reservation_sale')