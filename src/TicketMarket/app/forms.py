from django.utils import timezone
from django import forms
from .models import (driver,company,transport,station,route,station,routeStation,useraddress)
class DriverUpdataForm(forms.ModelForm):
    class Meta:
        model=driver
        fields=[
            'name',
            'surname'
        ]
class CompanyUpdataForm(forms.ModelForm):
    class Meta:
        model=company
        fields=[
            'name',
            'city',
            'user'
        ]
class StationUpdataForm(forms.ModelForm):
    class Meta:
        model=station
        fields=[
            'name',
            'city'
        ]
class TransportUpdataForm(forms.ModelForm):
    class Meta:
        model=transport
        fields=[
            'name',
            'description',
            'places',
            'company'
        ]
class useraddresstUpdataForm(forms.ModelForm):
    class Meta:
        model=useraddress
        fields = [
            'bulding',
            'apartment',
            'postcode',
            'street',
            'city',
            'phon',
        ]

class LineUpdataForm(forms.ModelForm):
    class Meta:
        model=route
        fields=[
            'title',
            'description',
            'tickets',
            'company',
            'transport',
            'driver'
        ]
class LineForm(forms.ModelForm):
    class Meta:
        model = routeStation
        fields = [
            'number',
            'price',
            'time',
            'station',
            'last'
        ]
    def clean_time(self):
        time = self.cleaned_data.get('time')
        if time < timezone.now():
            raise forms.ValidationError("You can't add past data")
        return time
    def clean_station(self):
        station = self.cleaned_data.get('station')
        if station is None:
            raise forms.ValidationError("Please choose station")
        return station
