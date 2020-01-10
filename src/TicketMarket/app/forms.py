from django import forms
from .models import (driver,company,transport,station)
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
            'city'
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
            'driver',
            'company'
        ]
