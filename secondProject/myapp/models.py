from django.db import models

# Create your models here.

class Tracking(models.Model):
    name = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)
    tracking = models.CharField(max_length=100, null=True, blank=True)
    other = models.TextField(null=True, blank=True)


    def __str__(self):
        return '{} - {} ({})'.format(self.name, self.tel, self.tracking)


class Position(models.Model):
    name = models.CharField(max_length=100)
    positon = models.CharField(max_length=100)
    salary = models.FloatField()

    def __str__(self):
        return 'name: {} - salary: {}'.format(self.name, self.salary)