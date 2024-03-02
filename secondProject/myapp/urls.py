from django.urls import path
from .views import Home, myShop, aboutUs, contactUs, tracking, ask, satisfy

urlpatterns = [
    path('', Home, name='home'),
    path("shop", myShop, name='shop'),
    path("aboutus", aboutUs, name='about-us'),
    path("contactus", contactUs, name='contact'),
    path("tracking", tracking, name='tracking'),
    path("satisfy", satisfy, name='satisfy'),
    path("ask", ask, name="ask")
]
