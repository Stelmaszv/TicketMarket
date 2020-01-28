from django.shortcuts import render,get_object_or_404,redirect
from .models import (route,driver,company,transport,station,transportticket)
from django.utils import timezone
from .forms import (DriverUpdataForm,CompanyUpdataForm,StationUpdataForm,TransportUpdataForm)
from django.views.generic.base import TemplateView
from django.views.generic import (UpdateView)
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from companymenager.views import mycompany
from core.baseview import (baseShowView)
class MainView(TemplateView):
    def get(self,request,*args,**kwargs):
        query=self.setSearch(request);
        context={'queryset':query,'request':request}
        return render(request,"home.html",context)
    def faindStart(self,start=False,destenation=False):
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
                    item.start=startnumber;
                    item.destenationnumber=destenationnumber
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
        tickets=len(item.tickets.all());
        places=item.transport.places
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
        return route.objects.all()
class BaseUpdateView(UpdateView):
    template_name = 'edit/editbase.html'
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(self.model, id=id_)
    def get(self,request,*args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = DriverUpdataForm(instance=obj)
            context['form'] = form
            context['items'] = mycompany().setData(request)
        return render(request, self.template_name, context)
class editTransport(BaseUpdateView):
    template_name = 'create/createTransport.html'
    form_class = TransportUpdataForm
    model=transport
class editDriver(BaseUpdateView):
    template_name = 'create/createdriver.html'
    form_class = DriverUpdataForm
    model=driver
class editCompany(BaseUpdateView):
    template_name = 'create/companycreate.html'
    form_class = CompanyUpdataForm
    model=company
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
class myprofil(TemplateView):
    template_name = 'myprofil.html'
class register(TemplateView):
    template_name = 'registeration/register.html'
    def post(self,request):
        register = UserCreationForm()
        if request.method=='POST':
            register= UserCreationForm(request.POST)
            if register.is_valid():
                register.save()
                username=register.cleaned_data['username']
                passsword=register.cleaned_data['password1']
                user=authenticate(username=username,passsword=passsword)
                login(request,user)
                return redirect('home')
        data= {'form':register}
        return render(request,self.template_name,data)





