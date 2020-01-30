from django.urls import path
from cart.views import (addtocart,mycart,shoping,addressed,summary,confirmation)
app_name = 'cart'
urlpatterns = [
    path('addToCart/<int:id>/<int:start>/<int:end>',addtocart.as_view(), name='addtocart'),
    path('addToCartindex/<int:id>/<int:start>/<int:end>',addtocart.as_view(), name='addtocartindex'),
    path('myCart/',mycart.as_view(), name='mycart'),
    path('shoping/',shoping.as_view(), name='shoping'),
    path('addressed/',addressed.as_view(), name='addressed'),
    path('summary/',summary.as_view(), name='summary'),
    path('confirmation/',confirmation.as_view(), name='confirmation')
]