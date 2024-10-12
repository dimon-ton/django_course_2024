from django.db import models

# Create your models here.


class Table(models.Model):
    number = models.IntegerField(unique=True)
    qr_code = models.ImageField(upload_to="qr-codes/")


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        