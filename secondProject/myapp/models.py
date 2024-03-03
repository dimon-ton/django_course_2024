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
    
class AskQA(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name='ชื่อผู้ติดต่อ')
    email = models.EmailField(null=True, blank=True, verbose_name="email")
    title = models.CharField(max_length=100, null=True, blank=True, verbose_name="หัวข้อ")
    detail = models.TextField(null=True, blank=True, verbose_name="รายละเอียด")


    def __str__(self):
        return '{} - {}'.format(self.name, self.title)
    

class SurveyResponse(models.Model):
    sex = models.CharField(max_length=10)
    age = models.IntegerField()
    education = models.CharField(max_length=50)
    offer = models.TextField()
    question_main = models.CharField(max_length=255)
    question_subtopic = models.CharField(max_length=255)
    response_value = models.IntegerField()

    def __str__(self):
        return f"{self.sex} - {self.age} - {self.education} - {self.question_main} - {self.question_subtopic}"