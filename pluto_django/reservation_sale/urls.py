from . import views
from django.urls import path

urlpatterns = [      
    path('', views.reservation_sale, name='reservation_sale'),
	path('reservation_sale_status_/<int:reservation_sale_id>/', views.change_status_reservation_sale, name='reservation_sale_status'),            
]