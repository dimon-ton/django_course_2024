from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def Home(req):
    return HttpResponse("<h1>hello world</h1>")


def myShop(req):
    return render(req, "myapp/home.html")

def aboutUs(req):
    return render(req, 'myapp/aboutus.html')

def contactUs(req):
    return render(req, 'myapp/contactus.html')