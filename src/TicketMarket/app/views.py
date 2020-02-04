from .models import (route,driver,company,transport,station)
from django.utils import timezone
from .forms import (DriverUpdataForm,CompanyUpdataForm,StationUpdataForm,TransportUpdataForm)
from django.views.generic.base import TemplateView
from django.contrib.auth.forms import UserCreationForm
from core.baseview import (baseListView,baseShowView,baseCreate,baseUpdateView)
from core.decorators import login_required,emptyCart,driverowner,copanyowner
class MainView(baseListView):
    template_name="home.html"
    def setContext(self,request):
        self.context = {'queryset': self.setSearch(request), 'request': request}
    def faindStart(self,start=False,destenation=False):
        query = route.objects.filter(stations__station__city=start).filter(stations__station__city=destenation)
        startnumber=0
        destenationnumber=0
        self.routs=[]
        for item in query:
            if item.active:
                soldOut = self.soldOut(item)
                for stationInItem in item.stations.all():
                    if stationInItem.station.city == start:
                        startnumber=stationInItem.number
                        Past = self.dataPast(stationInItem, start)
                    if stationInItem.station.city == destenation:
                        destenationnumber=stationInItem.number
                    if startnumber < destenationnumber:
                        item.start=startnumber;
                        item.destenationnumber=destenationnumber
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
        query=item.tickets.filter(invalid=False)
        tickets=len( query);
        places=item.transport.places
        print(str(tickets) + ' / ' +str(places))
        if tickets < places:
            return True
        return  False
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
        route().setLine()
        return route.objects.all()
class register(baseCreate):
    success_url = '/accounts/login/'
    template_name = 'registeration/register.html'
    form = UserCreationForm
class myprofil(TemplateView):
    template_name = 'myprofil.html'
class editTransport(baseUpdateView):
    template_name = 'create/createTransport.html'
    form = TransportUpdataForm
    getObject=transport
    @login_required
    def get(self,request,*args, **kwargs):
        return self.addGet(request)
class editCompany(baseUpdateView):
    template_name = 'create/companycreate.html'
    form = CompanyUpdataForm
    getObject=company
    @login_required
    @copanyowner
    def get(self,request,*args, **kwargs):
        return self.addGet(request)
class editDriver(baseUpdateView):
    template_name = 'create/createdriver.html'
    form = DriverUpdataForm
    getObject=driver
    @login_required
    @driverowner
    def get(self,request,*args, **kwargs):
        return self.addGet(request)
class editStation(baseUpdateView):
    template_name = 'edit/editbase.html'
    form = StationUpdataForm
    getObject  = station
    @login_required
    def get(self,request,*args, **kwargs):
        return self.addGet(request)
class show(baseShowView):
    template = 'show/show.html'
    getObject =route
    def setContext(self):
        self.obj=self.get_object()
        ticketAll = self.obj.tickets.filter(invalid=False)
        self.context = {'context': self.obj,'ticketAll': ticketAll}
class showDriver(baseShowView):
    template = 'show/showdriver.html'
    getObject = driver
class showCompany(baseShowView):
    template = 'show/showcompany.html'
    getObject = company
class showTransport(baseShowView):
    template = 'show/showtransport.html'
    getObject = transport
class showStation(baseShowView):
    template = 'show/showstation.html'
    getObject = station




