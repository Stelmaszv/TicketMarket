from django.shortcuts import redirect
from app.models import (cart,company,driver,route)
def login_required(func):
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        if args[1].user.is_anonymous:
            return redirect('/accounts/login/')
        return value
    return wrapper
def emptyCart(func):
    def wrapper(*args, **kwargs):
        cartitems=cart.objects.filter(buyer__username=args[1].user.username)
        if len(cartitems) ==0:
            return redirect('/cart/myCart/')
        value = func(*args, **kwargs)
        return value
    return wrapper
def driverowner(func):
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        id = kwargs['id']
        item = driver.objects.get(id=id).company.user
        if args[1].user!=item:
            return redirect('/company/')

        return value
    return wrapper
def copanyowner(func):
    def wrapper(*args, **kwargs):
        id=kwargs['id']
        item=company.objects.get(id=id)
        if args[1].user!=item.user:
            return redirect('/company/')
        value = func(*args, **kwargs)
        return value
    return wrapper
def route_owner(func):
    def wrapper(*args, **kwargs):
        id = kwargs['id']
        item=route.objects.get(id=id)
        if args[1].user != item.user:
            return redirect('/company/')
        value = func(*args, **kwargs)
        return value
    return wrapper