from django.db import models
from django.urls import reverse

class driver(models.Model):
    name=models.CharField(max_length=150)
    surname=models.CharField(max_length=150)
    def get_absolute_url(self):
        return reverse("driver", kwargs={"id": self.id})
class company(models.Model):
    name=models.CharField(max_length=150)
    city=models.CharField(max_length=150)
    def get_absolute_url(self):
        return reverse("company", kwargs={"id": self.id})
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
    driver = models.ForeignKey(driver, on_delete=models.SET_NULL, null=True, blank=True)
    company = models.ForeignKey(company, on_delete=models.SET_NULL, null=True, blank=True)
    def get_absolute_url(self):
        return reverse("transport", kwargs={"id": self.id})
class route(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    tickets = models.BigIntegerField(default=0)
    stations = models.ManyToManyField(routeStation)
    transport = models.ForeignKey(transport, on_delete=models.SET_NULL, null=True, blank=True)


