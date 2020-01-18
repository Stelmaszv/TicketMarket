from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic.base import TemplateView
from django.urls import reverse
from django.views.generic import (CreateView,DeleteView)
from app.models import (company,transport,driver,route,routeStation,station)
from app.forms import (CompanyUpdataForm,TransportUpdataForm,DriverUpdataForm,LineUpdataForm,LineForm)
from core.baseview import (baseShowView)
class mycompany(TemplateView):
    template_name = 'mycompany.html'
    def get(self,request,*args,**kwargs):
        items=self.setData(request)
        context={'items':items,'request':request}
        return render(request,self.template_name,context)
    def setData(self,request):
        current_user = request.user
        campanys=company.objects.filter(user__username=current_user.username)
        transports = transport.objects.filter(company__user__username=current_user.username)
        line = route.objects.filter(company__user__username=current_user.username)
        drivers = driver.objects.all()
        items={
            'campanys': campanys,
            'transports': transports,
            'drivers':drivers,
            'line':line
        }
        return items
class baseCreate(TemplateView):
    success_url = '/mycompany/'
    data=[]
    def get(self,request,id=None,*args, **kwargs):
        self.addget(request)
    def addget(self,request):
        self.setContext(request)
        return render(request, self.template_name, self.context)
    def setContext(self,request):
        self.items = mycompany().setData(request)
        register = self.form_class
        self.context = {'form': register, 'items': self.items, 'adddata': self.data}
class addcompany(baseCreate):
    template_name = 'create/companycreate.html'
    form_class = CompanyUpdataForm
class addtransport(baseCreate):
    template_name = 'create/createTransport.html'
    form_class = TransportUpdataForm
class addDriver(baseCreate):
    template_name = 'create/createdriver.html'
    form_class =  DriverUpdataForm
class createline(baseCreate):
    template_name = 'create/createline.html'
    form_class =  LineUpdataForm
    model = route;
    success_url = '/setline/12/';
    context={}
    def get(self, request,*args, **kwargs):
        self.setContext(request)
        return render(request, self.template_name,self.context)
    def post(self, request, *args, **kwargs):
        self.setContext(request)
        form = LineUpdataForm(request.POST)
        if form.is_valid():
            form.save()
            item=self.model.objects.latest('id')
            id=item.id
            self.success_url = '/mycompany/setline/' + str(id) + '/'
            return redirect(self.success_url)
        else:
            print('error')
        return render(request, self.template_name, self.context)
class setingsline(TemplateView):
    template_name = 'setline.html'
    def get(self, request, id=None, *args, **kwargs):
        line=route.objects.get(pk=id)
        route.setActive(line, id)
        data={
            'line':line,
            'stations':line.stations.all().order_by('number')
        }
        return render(request, self.template_name,data)
class addstationtoline(baseCreate):
    template_name = 'stationtoline.html'
    form_class = LineForm
    model = routeStation;
    def get(self, request, id=None, *args, **kwargs):
        self.success_url = '/mycompany/setline/'+str(id)+'/'
        self.data=self.setStations()
        return  self.addget(request)
    def post(self,request, id=None, *args, **kwargs):
        self.data = self.setStations()
        self.success_url = '/mycompany/setline/' + str(id) + '/'
        form = LineForm(request.POST)
        if form.is_valid():
            item=form.save()
            route.objects.get(id=id).stations.add(item)
            return  redirect(self.success_url)
        self.context={"form": form,'adddata': self.data}
        return render(request, self.template_name, self.context)
    def setStations(self):
        return  station.objects.all()
class deleteStation(DeleteView):
    template_name = 'delete/delete_line.html'
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(routeStation, id=id_)
    def post(self, request, id=None,line=None, *args, **kwargs):
        url = '/mycompany/setline/' + str(line) + '/'
        obj = self.get_object()
        obj.delete()
        return redirect(url)
class editStation(baseCreate):
    template_name = 'stationtoline.html'
    form_class = LineForm
    context={}
    model=LineForm
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(routeStation, id=id_)
    def post(self, request, id=None, *args, **kwargs):
        # POST method
        line_ = self.kwargs.get("line")
        self.success_url = '/mycompany/setline/' + str(line_) + '/'
        self.setContext()
        if self.form.is_valid():
            self.form.save()
            return redirect(self.success_url)
        else:
            print('dqd')
        return render(request, self.template_name, self.context)
    def get(self, request, id=None, *args, **kwargs):
        # GET method
        self.setContext()
        return render(request, self.template_name, self.context)
    def setContext(self):
        self.data = station.objects.all()
        self.obj = self.get_object()
        if self.obj is not None:
            self.form = LineForm(instance=self.obj)
            self.context['object'] = self.obj
            self.context['form'] = self.form
            self.context['adddata'] = self.data















