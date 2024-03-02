from django.shortcuts import render
from django.http import HttpResponse
from .models import Tracking, AskQA

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
    # track_list = ['ลุงวิศวกร - A1234',
    #               'สมหญิง - A1235',
    #               'สมชาย - A1236'
    #               ]

    track_list = Tracking.objects.all()
    print(track_list)
    context = {'tracking':track_list}

    return render(req, "myapp/tracking.html", context)

def ask(req):
    if req.method == 'POST':
        data = req.POST.copy()
        # print('data', data)
        name = data.get('name')
        email = data.get('email')
        title = data.get('title')
        detail = data.get('detail')


        QA_data = AskQA()
        QA_data.name = name
        QA_data.email = email
        QA_data.title = title 
        QA_data.detail = detail

        QA_data.save()



    return render(req, 'myapp/ask.html')

def satisfy(req):
    return render(req, "myapp/satisfy.html")