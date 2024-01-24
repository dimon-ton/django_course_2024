from django.urls import path
from .views import Home, myShop, aboutUs, contactUs

urlpatterns = [
    path('', Home, name='home'),
    path("shop", myShop, name='shop'),
    path("aboutus", aboutUs, name='about-us'),
    path("contactus", contactUs, name='contact'),
]
