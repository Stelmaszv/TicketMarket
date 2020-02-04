from app.models import (company,transport,driver,route,routeStation,station)
class data:
    def set(self,request):
        items={
            'campanys': company.objects.filter(user__username=request.user.username),
            'transports': transport.objects.filter(user__username=request.user.username),
            'drivers':driver.objects.filter(user__username=request.user.username),
            'line':route.objects.filter(company__user__username=request.user.username),
            'station':station.objects.all()
        }
        return items


