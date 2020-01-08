from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import route
from datetime import datetime
from django.utils import timezone
from django.views.generic.base import TemplateView
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
class show(TemplateView):
    def get(self,request,*args,**kwargs):
        context={'routs':self.get_object()}
        return render(request,"show.html",context)
    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(route, id=id)
        return obj