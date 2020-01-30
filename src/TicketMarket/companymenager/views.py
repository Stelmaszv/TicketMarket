from django.shortcuts import render,redirect,get_object_or_404,HttpResponse,reverse
from core.getData import data
from core.baseview import baseListView,baseCreate,baseUpdateView,baseDeleteView
from app.models import (company,transport,driver,route,routeStation,station)
from app.forms import (CompanyUpdataForm,TransportUpdataForm,DriverUpdataForm,LineUpdataForm,AddstationToline)
class mycompany(baseListView):
    template_name = 'mycompany.html'
    def setContext(self,request):
        items = data().set(request)
        self.context = {
            'items': items,
            'request': request
        }
class setingsline(baseListView):
    template_name = 'setline.html'
    def setContext(self,request):
        id = self.kwargs.get("id")
        line = route.objects.get(pk=id)
        route.setActive(line, id)
        self.context = {
            'line': line,
            'stations': line.stations.all().order_by('number')
        }
class addcompany(baseCreate):
    template_name = 'create/companycreate.html'
    form = CompanyUpdataForm
class addtransport(baseCreate):
    template_name = 'create/createTransport.html'
    form = TransportUpdataForm
class addDriver(baseCreate):
    template_name = 'create/createdriver.html'
    form =  DriverUpdataForm
class createline(baseCreate):
    template_name = 'create/createline.html'
    form =  LineUpdataForm
    model = route;
    def postSave(self):
        item = self.model.objects.latest('id')
        id = item.id
        self.success_url = '/mycompany/setline/' + str(id) + '/'
class addstationtoline(baseCreate):
    template_name = 'stationtoline.html'
    form = AddstationToline
    def postInit(self, request, *args, **kwargs):
        id = self.kwargs.get("id")
        self.success_url = '/mycompany/setline/' + str(id) + '/'
    def postSave(self, request, *args, **kwargs):
        id = self.kwargs.get("id")
        route.objects.get(id=id).stations.add(self.item)
class editStation(baseUpdateView):
    template_name = 'stationtoline.html'
    form_class = AddstationToline
    getObject= routeStation
    def get_success_url(self):
        line_ = self.kwargs.get("line")
        return reverse('mycompany:setline', kwargs={'id': line_})
class deleteStation(baseDeleteView):
    template_name = 'delete/delete_line.html'
    getObject = routeStation
    def get_success_url(self):
        id_ = self.kwargs.get("line")
        return reverse('mycompany:setline', kwargs={'id': id_})

















