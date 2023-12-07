from . import views
from django.urls import path

urlpatterns = [      
    path('', views.reservation_cabin, name='reservation_cabin'),
		path('reservation_cabin_status_/<int:reservation_cabin_id>/', views.change_status_reservation_cabin, name='reservation_cabin_status'),            
]