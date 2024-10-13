from django.urls import path

from .views import *


urlpatterns = [
    path('test_pos', test_pos, name='test_pos'),
    path('tables/', AllTable, name='all-tables'),
]