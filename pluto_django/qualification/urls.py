from . import views
from django.urls import path

urlpatterns = [      
    path('', views.qualification, name='qualification'),
		path('qualification_status_/<int:qualification_id>/', views.change_status_qualification, name='qualification_status'),            
]