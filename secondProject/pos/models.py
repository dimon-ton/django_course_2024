from django.db import models
import qrcode
from django.conf import settings
import os
# Create your models here.


class Table(models.Model):
    number = models.IntegerField(unique=True)
    qr_code = models.ImageField(upload_to="qr-codes/", null=True, blank=True)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.generate_qr_code()


    def generate_qr_code(self):
        url = f"{settings.SITE_URL}/pos/order/{self.id}/"
        qr = qrcode.make(url)
        qr_code_path = f"qr_codes/table_{self.id}.png"

        # if the qr_code folder does not exist, create it
        if not os.path.exists(os.path.join(settings.MEDIA_ROOT, "qr_codes")):
            os.makedirs(os.path.join(settings.MEDIA_ROOT, "qr_codes"))

        qr.save(os.path.join(settings.MEDIA_ROOT, qr_code_path))
        self.qr_code = qr_code_path
        super().save()

    def __str__(self):
        return f"{self.number}"
    

class Category(models.Model):
    name = models.CharField(max_length=150)
    images = models.ImageField(upload_to="category-images/")

    def __str__(self):
        return f"{self.name}"

class Menu(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=1)
    available = models.BooleanField(default=True)
    images = models.ImageField(upload_to="menu-images/")
    unit = models.CharField(max_length=20, default="แก้ว")

    def __str__(self):
        return self.name


class OrderMenu(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    menu = models.ManyToManyField(Menu)
    total_buyer_price = models.FloatField(default=0)
    count = models.IntegerField(default=1)
    vat = models.FloatField(default=0)
    final_price_with_vat = models.FloatField(default=0)
    order_date = models.DateTimeField(auto_now_add=True)
    order_time = models.TimeField(auto_now_add=True)

    status = models.CharField(max_length=20, choices=[
        ('pending', 'รอดำเนินการ'), 
        ('in_progress', 'อยู่ระหว่างดำเนินการ'), 
        ('complete', 'เสร็จเรียบร้อย'),
        ])

    def __str__(self):
        return f"{self.table.number} {self.menu.name}"




class OrderMenuItem(models.Model):
    order_menu = models.ForeignKey(OrderMenu, on_delete=models.CASCADE, related_name="order_items")
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    count = models.IntegerField()
    item_total = models.FloatField(default=0)


    def __str__(self):
        return f"{self.order_menu.table.number} {self.menu.name}"