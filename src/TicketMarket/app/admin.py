from django.contrib import admin
from .models import (route,driver,company,station,routeStation,transport)
admin.site.register(route)
admin.site.register(driver)
admin.site.register(company)
admin.site.register(station)
admin.site.register(routeStation)
admin.site.register(transport)