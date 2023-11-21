from . import views
from django.urls import path

urlpatterns = [      
    path('', views.Customer, name='Customer'), 
    path('Customer_status_/<int:Customer_id>/', views.change_status_Customer, name='Customer_status'),           
]