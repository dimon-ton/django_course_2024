from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

def test_pos(req):
    return HttpResponse("<h1>test_pos</h1>")