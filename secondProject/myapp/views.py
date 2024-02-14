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

def tracking(req):
    track_list = ['ลุงวิศวกร - A1234',
                  'สมหญิง - A1235',
                  'สมชาย - A123'
                  ]
    
    context = {'tracking':track_list}

    return render(req, "myapp/tracking.html", context)