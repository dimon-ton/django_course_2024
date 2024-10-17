from django.urls import path

from .views import *


urlpatterns = [
    path('test_pos', test_pos, name='test_pos'),
    path('tables/', AllTable, name='all-tables'),
    path('order/<int:table_id>/', OrdersMenu, name='order-menu'),
    path('monthly-order-summary', MonthlyOrderSummary, name='monthly-order-summary'),
]