"""
URL configuration for pluto_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('Customer/', include('Customer.urls')),
    path('facilities/', include('facilities.urls')),
    path('typeCabin/', include('typeCabin.urls')),
    path('services/', include('services.urls')),
    path('cabin/', include('cabin.urls')),
    path('reservation_sale/', include('reservation_sale.urls')),  
    path('cabin_facility/', include('cabin_facility.urls')),
    path('payment/', include('payment.urls')),
    path('qualification/', include('qualification.urls')),
    path('reservation_services/', include('reservation_services.urls')),
    path('reservation_cabin/', include('reservation_cabin.urls')), 
]