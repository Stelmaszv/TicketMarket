"""TicketMarket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from app.views import (MainView,show,showDriver,showCompany,showTransport,showStation,editDriver,editCompany,editTransport,editStation)

urlpatterns = [
    path('', MainView.as_view()),
    path('show/<int:id>', show.as_view()),
    path('show/driver/<int:id>/', showDriver.as_view() ,name = 'driver'),
    path('show/driver/<int:id>/edit/', editDriver.as_view() ,name = 'driveredit'),
    path('show/company/<int:id>/', showCompany.as_view(),name = 'company'),
    path('show/company/<int:id>/edit/', editCompany.as_view() ,name = 'companyedit'),
    path('show/transport/<int:id>/', showTransport.as_view() ,name='transport'),
    path('show/transport/<int:id>/edit/', editTransport.as_view() ,name='transportedit'),
    path('show/station/<int:id>/', showStation.as_view() ,name='station'),
    path('show/station/<int:id>/edit/',editStation.as_view() ,name='stationedit'),
    path('admin/', admin.site.urls),
]
