from django.shortcuts import render,get_object_or_404
from app.models import (route,cart,payment,shipping,useraddress,transportticket,transportticketstan)
from app.forms import (useraddresstUpdataForm)
from core.baseview import (baseListView,baseUpdateView)
from core.decorators import login_required,emptyCart
class ticket:
    def __init__(self,line,start,end):
        self.start=start
        self.end=end
        self.line=line
        self.prices={}
    def setPrice(self):
        index=0
        roudPrice=0
        stationOnLine=[]
        classList=[]
        indexinclass=-1
        for item in self.line.stations.all():
            if item.number >= self.start and  item.number <= self.end:
                stationOnLine.append(item)
        for item in stationOnLine:
            if index>0:
                first=stationOnLine[index].time
                secunds = stationOnLine[index-1].time
                price=first-secunds
                roudPrice=roudPrice+price.total_seconds()
            index=index+1
        for item in self.line.transport.classs.all():
            item.classPrice=item.level*roudPrice/10
            classList.append(item)
            indexinclass=indexinclass+1
            item.indexinclass=indexinclass
        return classList
class addtocart(baseListView):
    template_name = 'cart/addtocart.html'
    success_url = '/cart/myCart/'
    @login_required
    def get(self, request, *args, **kwargs):
        return self.addGet(request)
    def setContext(self,request):
        price= self.setPrice(request)
        self.context={
            'prices':price,
            'parms':{
                'id'   : self.kwargs.get("id"),
                'start': self.kwargs.get("start"),
                'end'  : self.kwargs.get("end"),
                'index': self.kwargs.get("index")
            }
        }
    def setPrice(self,request,index=None):
        id=self.kwargs.get("id")
        line = route.objects.get(pk=id)
        price = ticket(line, self.kwargs.get("start"), self.kwargs.get("end"))
        prices = price.setPrice();
        if request.GET:
            item = prices[int(request.GET['index'])]
            newcart = cart(name=item.name, price=item.classPrice, quantity=1, route=line, buyer=request.user)
            newcart.save()
            self.redirect=True
        return prices
class mycart(baseListView):
    template_name = 'cart/mycart.html'
    @login_required
    def get(self,request,*args, **kwargs):
        return self.addGet(request)
    def setContext(self,request):
        self.context={
            'list':cart.objects.filter(buyer__username=request.user.username)
        }
class shoping(baseListView):
    template_name = 'order/shipping.html'
    @login_required
    @emptyCart
    def get(self,request,*args, **kwargs):
        return self.addGet(request)
    def setContext(self,request):
        self.context = {
            'shipping': shipping.objects.all(),
            'payment': payment.objects.all()
        }
        if request.GET:
            self.success_url = '/cart/addressed/?payment'+str(request.GET['payment'])+'&&shipping='+str(request.GET['shipping'])
            self.redirect = True
class addressed(baseUpdateView):
    template_name = 'order/addressed.html'
    form = useraddresstUpdataForm
    getObject = useraddress
    success_url = '/cart/summary/?payment=1&&shipping=1'
    @login_required
    @emptyCart
    def get(self, request, *args, **kwargs):
        return self.addGet(request)
    def get_object(self):
        return get_object_or_404(useraddress, user__username=self.request.user)
class summary(baseListView):
    template_name = 'order/summary.html'
    @login_required
    @emptyCart
    def get(self, request, *args, **kwargs):
        return self.addGet(request)
    def setContext(self,request):
        self.context = {
            'payment': payment.objects.get(id=int(request.GET['payment'])),
            'shipping': shipping.objects.get(id=int(request.GET['shipping'])),
            'address': useraddress.objects.get(user__username=request.user.username),
            'cartObj': cart.objects.filter(buyer__username=request.user.username)
        }
class confirmation(baseListView):
    template_name = 'order/confirmation.html'
    @login_required
    @emptyCart
    def get(self, request, *args, **kwargs):
        return self.addGet(request)
    def setContext(self, request):
        self.context = {}
        self.orderExecute(request)
    def orderExecute(self,request):
        cartObj = cart.objects.filter(buyer__username=request.user.username)
        for cartelment in cartObj:
            el=transportticket(name=cartelment.name, price=cartelment.price, stan=transportticketstan.objects.get(id=1),route=cartelment.route,buyer=request.user,company=cartelment.route.company)
            el.save()
            routeElemnt=route.objects.get(id=cartelment.route.id)
            routeElemnt.tickets.add(el)
            routeElemnt.save()
            cartelment.delete()
        return render(request, 'order/confirmation.html',self.context)


