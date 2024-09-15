from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
admin.site.register(Tracking)
admin.site.register(Position)
admin.site.register(AskQA)
admin.site.register(SurveyResponse)
admin.site.register(Score)


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ("body",)
    list_display = ["id", "title", "images"]
    list_editable = ["title"]

admin.site.register(Author)
admin.site.register(Post, PostAdmin)


class ProductAdmin(SummernoteModelAdmin):
    summernote_fields = ("detail")
    list_display = ["id", "name", "available"]
    list_editable = ["name"]



class OrderAdmin(admin.ModelAdmin):
    list_display = ["id","products"]

admin.site.register(Order, OrderAdmin) 

class TrackingOrderIDAdmin(admin.ModelAdmin):
    list_display = ["id", "tracking_order"]

admin.site.register(TrackingOrderID, TrackingOrderIDAdmin)

admin.site.register(Product, ProductAdmin)

admin.site.register(Category)

admin.site.register(Profile)
admin.site.register(Discount)


class CartAdmin(admin.ModelAdmin):
    list_display = ['product_name']

admin.site.register(Cart, CartAdmin)

class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['product_name']

admin.site.register(OrderProduct, OrderProductAdmin)

class CartOrderAdmin(admin.ModelAdmin):
    list_display =['user', 'first_name', 'last_name']

admin.site.register(CartOrder, CartOrderAdmin)


# ///////////////////// เพิ่มใหม่ ////////////////////////
class MachineAdmin(admin.ModelAdmin):
    list_display =['name', 'model', 'year']

admin.site.register(Machine, MachineAdmin)


class ReservationAdmin(admin.ModelAdmin):
    list_display =['customer_name', 'tel', 'email']

admin.site.register(Reservation, ReservationAdmin)


class CommentsAdmin(admin.ModelAdmin):
    list_display =['content', 'name', 'email']

admin.site.register(Comments, CommentsAdmin)