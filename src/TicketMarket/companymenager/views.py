from django.shortcuts import render,redirect,get_object_or_404,HttpResponse,reverse
from core.getData import data
from core.baseview import baseListView,baseCreate,baseUpdateView,baseDeleteView,baseShowView
from app.models import (company,transport,driver,route,routeStation,station,transportticket,transportticketstan)
from app.forms import (CompanyUpdataForm,TransportUpdataForm,DriverUpdataForm,LineUpdataForm,AddstationToline)
from django.views.generic.base import TemplateView
from core.decorators import login_required,emptyCart,copanyowner,route_owner
class mycompany(baseListView):
    template_name = 'mycompany.html'
    @login_required
    def get(self, request, *args, **kwargs):
        return self.addGet(request)
    def setContext(self,request):
        items = data().set(request)
        self.context = {
            'items': items,
            'request': request
        }
class companybilans(baseListView):
    template_name = 'show/companybilans.html'
    @login_required
    @copanyowner
    def get(self, request, *args, **kwargs):
        return self.addGet(request)
    def setContext(self,request):
        id = self.kwargs.get("id")
        items = route.objects.filter(company__id=id)
        self.context = {
            'items': items,
        }
class mytickets(baseListView):
    template_name = 'show/mytickets.html'
    @login_required
    def get(self, request, *args, **kwargs):
        return self.addGet(request)
    def setContext(self, request):
        self.context = {
            'items': transportticket.objects.filter(buyer__username=request.user.username),
        }
class ticketsDetails(baseShowView):
    template = 'show/ticketsDetail.html'
    getObject = transportticket
class updatestan(TemplateView):
    @login_required
    @route_owner
    def get(self,request,id=None,*args,**kwargs):
        item=transportticket.objects.get(pk=id)
        if item.stan.id == 2:
            item.stan=transportticketstan.objects.get(pk=1)
        else:
            item.stan = transportticketstan.objects.get(pk=2)
        item.save()
        return redirect('/mycompany/ticket/'+str(id))
class routTickets(baseListView):
    template_name = 'show/routTickets.html'
    @login_required
    def get(self, request, *args, **kwargs):
        return self.addGet(request)
    def setContext(self,request):
        id = self.kwargs.get("id")
        items = route.objects.get(pk=id)
        self.context = {
            'items': items.tickets.all(),
        }
class setingsline(baseListView):
    template_name = 'setline.html'
    @login_required
    def get(self, request, *args, **kwargs):
        return self.addGet(request)
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
    @login_required
    def get(self, request, *args, **kwargs):
        return self.addGet(request)
class addtransport(baseCreate):
    template_name = 'create/createTransport.html'
    form = TransportUpdataForm
    @login_required
    def get(self, request, *args, **kwargs):
        return self.addGet(request)
class addDriver(baseCreate):
    template_name = 'create/createdriver.html'
    form =  DriverUpdataForm
    @login_required
    def get(self, request, *args, **kwargs):
        return self.addGet(request)
class createline(baseCreate):
    template_name = 'create/createline.html'
    form =  LineUpdataForm
    model = route;
    @login_required
    def get(self, request, *args, **kwargs):
        return self.addGet(request)
    def postSave(self):
        item = self.model.objects.latest('id')
        id = item.id
        self.success_url = '/mycompany/setline/' + str(id) + '/'
class addstationtoline(baseCreate):
    template_name = 'stationtoline.html'
    form = AddstationToline
    @login_required
    @route_owner
    def get(self, request, *args, **kwargs):
        return self.addGet(request)
    def postInit(self, request, *args, **kwargs):
        id = self.kwargs.get("id")
        self.success_url = '/mycompany/setline/' + str(id) + '/'
    def postSave(self, request, *args, **kwargs):
        id = self.kwargs.get("id")
        route.objects.get(id=id).stations.add(self.item)
class editStation(baseUpdateView):
    template_name = 'stationtoline.html'
    form = AddstationToline
    getObject= routeStation
    @login_required
    def get(self, request, *args, **kwargs):
        return self.addGet(request)
    def get_success_url(self):
        line_ = self.kwargs.get("line")
        return reverse('mycompany:setline', kwargs={'id': line_})
class deleteStation(baseDeleteView):
    template_name = 'delete/delete_line.html'
    getObject = routeStation
    @login_required
    def get(self, request, *args, **kwargs):
        return self.addGet(request)
    def get_success_url(self):
        id_ = self.kwargs.get("line")
        return reverse('mycompany:setline', kwargs={'id': id_})

















