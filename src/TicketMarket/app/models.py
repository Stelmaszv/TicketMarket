from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone

class classintrnasport(models.Model):
    name=models.CharField(max_length=150)
    level=models.BigIntegerField()
class company(models.Model):
    name=models.CharField(max_length=150)
    city=models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    def get_absolute_url(self):
        return reverse("company", kwargs={"id": self.id})
class driver(models.Model):
    name=models.CharField(max_length=150)
    surname=models.CharField(max_length=150)
    company = models.ForeignKey(company, on_delete=models.SET_NULL, null=True, blank=True)
    def get_absolute_url(self):
        return reverse("driver", kwargs={"id": self.id})
class station(models.Model):
    name = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    def get_absolute_url(self):
        return reverse("station", kwargs={"id": self.id})
class routeStation(models.Model):
    number = models.BigIntegerField()
    price = models.DecimalField(max_digits=100, decimal_places=2,null=True, blank=True)
    time = models.DateTimeField()
    station = models.ForeignKey(station, on_delete=models.SET_NULL, null=True, blank=True)
    last= models.BooleanField(default=False)
    def get_absolute_url(self):
        return reverse("driver", kwargs={"id": self.id})
class transport(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    places = models.BigIntegerField(default=0)
    company = models.ForeignKey(company, on_delete=models.SET_NULL, null=True, blank=True)
    classs = models.ManyToManyField(classintrnasport, blank=True)
    def get_absolute_url(self):
        return reverse("transport", kwargs={"id": self.id})
class route(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    tickets = models.BigIntegerField(default=0)
    stations = models.ManyToManyField(routeStation, blank=True)
    company = models.ForeignKey(company, on_delete=models.SET_NULL, null=True, blank=True)
    transport = models.ForeignKey(transport, on_delete=models.SET_NULL, null=True, blank=True)
    driver = models.ForeignKey(driver, on_delete=models.SET_NULL, null=True, blank=True)
    active= models.BooleanField(default=False,blank=True)
    def setActive(self,id):
        error=0
        item=route.objects.get(id=id)
        allStations=len(item.stations.all())
        if allStations > 2:
            ifcorectTime = self.ifcorectTime(allStations)
            lastitem = item.stations.all().order_by('-number')
            if ifcorectTime:
                error = error + 1
            if lastitem[0].time < timezone.now():
                error = error + 1
        else:
            error = error + 1
        if error < 1:
            self.active=True;
        else:
            self.active =False;
        self.save()
    def ifcorectTime(self,station):
        index=0
        error=0
        for item in station:
            if index > 0:
                if station[index].time < station[index-1].time:
                    error=error+1
            index=index+1
        if error < 1:
            return False
        return True
class cart(models.Model):
    name = models.CharField(max_length=250)
    price = models.BigIntegerField(default=0)
    quantity = models.BigIntegerField(default=0)
    route = models.ForeignKey(route, on_delete=models.SET_NULL, null=True, blank=True)
    buyer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
class shipping(models.Model):
    name = models.CharField(max_length=250)
    price = models.BigIntegerField(default=0)
class payment(models.Model):
    name = models.CharField(max_length=250)
    price = models.BigIntegerField(default=0)

