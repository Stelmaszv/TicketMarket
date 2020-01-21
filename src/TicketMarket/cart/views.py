from django.shortcuts import render, redirect,HttpResponse,reverse
from django.views.generic.base import TemplateView
from app.models import (route,cart,payment,shipping)
import datetime
from django.utils import timezone

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
class addtocart(TemplateView):
    template_name = 'cart/addtocart.html'
    def get(self,request, id=None,start=None,end=None,index=None, *args, **kwargs):
        line=route.objects.get(pk=id)
        price=ticket(line,start,end)
        prices=price.setPrice();
        if index:
            if index>-1:
                item=prices[index]
                newcart=cart(name=item.name, price=item.classPrice, quantity=1,route=line,buyer=request.user)
                newcart.save()
                return redirect('/cart/myCart/')
        context={
            'classs':prices,
            'parms':{
                'id'   : id,
                'start':start,
                'end':end,
                'index':index
            }
        }

        return render(request, self.template_name,context)
class addToCartAction(TemplateView):
    template_name = 'cart/addtocart.html'
    def get(self, request, id=None, start=None, end=None, *args, **kwargs):
        prices=request.COOKIES.get('prices')
        return render(request, self.template_name,{})
class mycart(TemplateView):
    template_name = 'cart/mycart.html'
    def get(self, request, id=None, start=None, end=None, *args, **kwargs):
        list=cart.objects.filter(buyer__username=request.user.username)
        context = {
            'list':list
        }
        return render(request, self.template_name, context)
class order(TemplateView):
    def get(self, request, step=None, *args, **kwargs):
        items=[shoping,addressed,summary,confirmation]
        return items[step].get(self,request)
class shoping(TemplateView):
    def get(self,request):
        if request.GET:
            if request.GET['shipping'] and request.GET['payment']:
                shippingGET=request.GET['shipping']
                paymentGET=request.GET['payment']
                return redirect('/cart/orderproces/1')
        context = {
            'shipping':shipping.objects.all(),
            'payment':payment.objects.all()
        }
        return render(request, 'order/shipping.html', context)
class addressed:
    def get(self,request):
        context = {}
        return render(request, 'order/addressed.html', context)
class summary:
    def get(self,request):
        context = {}
        return render(request, 'order/summary.html', context)
class confirmation:
    def get(self,request):
        context = {}
        return render(request, 'order/confirmation.html', context)

