from . import views
from django.urls import path

urlpatterns = [      
    path('', views.typeCabin, name='typeCabin'),  
    path('typeCabin_status_/<int:typeCabin_id>/', views.change_status_typeCabin, name='typeCabin_status'),  
    path('create/', views.create_typeCabin, name='create_typeCabin'),         
]