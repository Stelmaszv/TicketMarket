from django.urls import path
from companymenager.views import (mycompany,addcompany,addtransport,addDriver,createline,setingsline,addstationtoline,deleteStation,editStation)
app_name = 'mycompany'
urlpatterns = [
    path('',mycompany.as_view() ,name='mycompany'),
    path('addcampany/',addcompany.as_view() ,name='addcampany'),
    path('addTransport/',addtransport.as_view() ,name='addtransport'),
    path('adddriver/',addDriver.as_view() ,name='adddriver'),
    path('addline/',createline.as_view() ,name='addline'),
    path('setline/<int:id>/',setingsline.as_view()  ,name='setline'),
    path('editline/<int:id>/',setingsline.as_view()  ,name='editline'),
    path('addstationtoline/<int:id>/',addstationtoline.as_view()  ,name='addstationtoline'),
    path('deleteStation/<int:line>/<int:id>/',deleteStation.as_view() ,name='deleteStation'),
    path('editStation/<int:line>/<int:id>/',editStation.as_view() ,name='editStation')
]