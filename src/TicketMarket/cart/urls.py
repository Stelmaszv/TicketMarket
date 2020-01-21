from django.urls import path
from cart.views import (addtocart,addToCartAction,mycart,order)
app_name = 'cart'
urlpatterns = [
    path('addToCart/<int:id>/<int:start>/<int:end>',addtocart.as_view(), name='addtocart'),
    path('addToCartindex/<int:id>/<int:start>/<int:end>/<int:index>',addtocart.as_view(), name='addtocartindex'),
    path('myCart/',mycart.as_view(), name='mycart'),
    path('orderproces/<int:step>',order.as_view(), name='orderproces'),
]