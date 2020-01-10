from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from .models import (route,driver,company,transport,station)
from datetime import datetime
from django.utils import timezone
from .forms import (DriverUpdataForm,CompanyUpdataForm,StationUpdataForm,TransportUpdataForm)
from django.views.generic.base import TemplateView
from django.views.generic import (
    UpdateView,
)
class AboutView(TemplateView):
    def get(self,request,*args,**kwargs):
        query=self.setSearch(request);
        context={'queryset':query,'request':request}
        return render(request,"home.html",context)
    def faindStart(self,start,destenation):
        query = route.objects.filter(stations__station__city=start).filter(stations__station__city=destenation)
        startnumber=0
        destenationnumber=0
        self.routs=[]
        for item in query:
            soldOut=self.soldOut(item)
            for stationInItem in item.stations.all():
                Past=self.dataPast(stationInItem,start)
                if stationInItem.station.city == start:
                    startnumber=stationInItem.number
                if stationInItem.station.city == destenation:
                    destenationnumber=stationInItem.number
                if startnumber is not None and destenationnumber is not None:
                    if startnumber < destenationnumber:
                        if Past and soldOut:
                            self.addItem(item)
        return self.routs
    def setNumber(self,item,place):
        if item.station.city == place:
            return item.number
        return False
    def dataPast(self,item,start):
        if item.station.city == start:
            if item.time < timezone.now():
                return False
            return True
    def soldOut(self,item):
        if item.tickets == item.transport.places:
            return False
        return True
    def addItem(self,item):
        count=0;
        for el in self.routs:
            if el.id==item.id:
                count=count+1;
        if count==0:
            self.routs.append(item)
    def setSearch(self,request):
        if request.GET:
            if len(request.GET['destenation']) and len(request.GET['start']):
                return self.faindStart(request.GET['start'],request.GET['destenation'])
        return route.objects.all()
class baseShowView(TemplateView):
    def get(self,request,*args,**kwargs):
        context={'context':self.get_object()}
        return render(request,self.template,context)
    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(self.model, id=id)
        return obj
class BaseUpdateView(UpdateView):
    template_name = 'edit/editbase.html'
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(self.model, id=id_)
class editDriver(BaseUpdateView):
    form_class = DriverUpdataForm
    model=driver
class editCompany(BaseUpdateView):
    form_class = CompanyUpdataForm
    model=company
class editTransport(BaseUpdateView):
    form_class = TransportUpdataForm
    model=transport
class editStation(BaseUpdateView):
    form_class = StationUpdataForm
    model=station
class show(baseShowView):
    template = 'show/show.html'
    model=route
class showDriver(baseShowView):
    template = 'show/showdriver.html'
    model = driver
class showCompany(baseShowView):
    template = 'show/showcompany.html'
    model = company
class showTransport(baseShowView):
    template = 'show/showtransport.html'
    model = transport
class showStation(baseShowView):
    template = 'show/showstation.html'
    model = station


