from django.shortcuts import render,redirect,get_object_or_404,HttpResponse,reverse
from django.views.generic.base import TemplateView
from django.views.generic import (DeleteView,UpdateView)
from app.models import (company,transport,driver,route,routeStation,station)
from app.forms import (CompanyUpdataForm,TransportUpdataForm,DriverUpdataForm,LineUpdataForm,AddstationToline)
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
        stations = station.objects.all()
        drivers = driver.objects.all()
        items={
            'campanys': campanys,
            'transports': transports,
            'drivers':drivers,
            'line':line,
            'station':stations
        }
        return items
class baseCreate(TemplateView):
    success_url = '/mycompany/'
    data=[]
    def get(self,request,id=None,*args, **kwargs):
        return self.addget(request)
    def addget(self,request):
        self.setContext(request)
        self.form = self.setform(request)
        return render(request, self.template_name, self.context)
    def setContext(self,request):
        self.items = mycompany().setData(request)
        self.context = {'form': self.form, 'items': self.items, 'adddata': self.data}
    def post(self,request, *args, **kwargs):
        self.setContext(request)
        self.form = self.setform(request)
        if self.form.is_valid():
            return self.basePostusbmit(request)
        else:
            self.setContext(request)
            return render(request, self.template_name, self.context)
        return render(request, self.template_name, self.context)
    def basePostusbmit(self,request):
        self.postInit(request)
        self.item=self.form.save()
        self.postSave(request)
        return redirect(self.success_url)
    def setform(self,request):
        return self.form(request.POST)
    def postInit(self,request,*args, **kwargs):
        pass
    def postSave(self,request, *args, **kwargs):
        pass
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
class editStation(UpdateView):
    template_name = 'stationtoline.html'
    form_class = AddstationToline
    getObject = routeStation
    def get_success_url(self):
        line_ = self.kwargs.get("line")
        return reverse('mycompany:setline', kwargs={'id': line_})
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(self.getObject, id=id_)
class deleteStation(DeleteView):
    template_name = 'delete/delete_line.html'
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(routeStation, id=id_)
    def get_success_url(self):
        id_ = self.kwargs.get("line")
        return reverse('mycompany:setline', kwargs={'id': id_})
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
















