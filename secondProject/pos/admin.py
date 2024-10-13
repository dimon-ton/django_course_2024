from django.contrib import admin
from .models import *

# Register your models here.

class TableAdmin(admin.ModelAdmin):
    list_display = ("number", "qr_code")


admin.site.register(Table, TableAdmin)