from django.urls import path
from .views import *

urlpatterns = [
    path('', Home, name='home'),
    path("shop", myShop, name='shop'),
    path("aboutus", aboutUs, name='about-us'),
    path("contactus", contactUs, name='contact'),
    path("tracking", tracking, name='tracking'),
    path("satisfy", satisfy, name='satisfy'),
    path("ask", ask, name="ask"),
    path("questions", question, name="questions"),
    path("anwser/<int:askid>", anwser, name="answer"),
    path("blogs", PostPage, name="post"),
    path("blog-detail/<slug:slug>/", postDetail, name="blog-detail"),
    # register and login page  
    path("register", register, name="register"),  
]
