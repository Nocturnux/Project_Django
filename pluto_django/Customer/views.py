from django.shortcuts import render, redirect

from Customer.models import customer

def Customer(request):
    Customer_list = customer.objects.all()
    return render(request, 'Customer/index.html', {'Customer_list': Customer_list})


def change_status_Customer(request, Customer_id):
    Customer = customer.objects.get(pk=Customer_id)
    Customer.status = not Customer.status
    Customer.save()
    return redirect('Customer')
