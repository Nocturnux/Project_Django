from . import views
from django.urls import path

urlpatterns = [      
    path('', views.reservation_services, name='reservation_services'),
		path('reservation_service_status_/<int:reservation_service_id>/', views.change_status_reservation_service, name='reservation_service_status'),            
]