from . import views
from django.urls import path

urlpatterns = [      
    path('', views.cabin_facility, name='cabin_facility'),
		path('cabin_facility_status_/<int:cabin_facility_id>/', views.change_status_cabin_facility, name='cabin_facility_status'),            
]