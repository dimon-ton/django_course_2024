from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def test_pos(req):
    return HttpResponse("<h1>test_pos</h1>")


def AllTable(req):
    try:
        all_table = Table.objects.all()
    except Table.DoesNotExist:
        all_table = None

    context = {"all_table": all_table}

    return render(req, "pos/all-tables.html", context)