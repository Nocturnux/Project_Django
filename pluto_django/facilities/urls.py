from . import views
from django.urls import path

urlpatterns = [      
    path('', views.facilities, name='facilities'),
    path('facilities_status_/<int:facilities_id>/', views.change_status_facilities, name='facilities_status'),            
]            