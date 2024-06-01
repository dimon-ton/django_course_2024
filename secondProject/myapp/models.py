from django.db import models
from taggit.managers import TaggableManager

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
    name = models.CharField(max_length=100, verbose_name='ชื่อผู้ติดต่อ')
    email = models.EmailField(null=True, blank=True, verbose_name="email")
    title = models.CharField(max_length=100, null=True, blank=True, verbose_name="หัวข้อ")
    detail = models.TextField(null=True, blank=True, verbose_name="รายละเอียด")
    detail_answer = models.TextField(null=True, blank=True, verbose_name="คำตอบ")


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
    

class Score(models.Model):
    survey = models.ForeignKey(SurveyResponse, on_delete=models.CASCADE)
    score = ['test1', 'test1']


    test1 = models.IntegerField()

    def __str__(self):
        return f'{self.survey}'
    

class Author(models.Model):
    author_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='author-image/', null=True, blank=True, default="default.png")


    def __str__(self):
        return self.author_name

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=280, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    images = models.ImageField(upload_to='post-image/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, max_length=180, null=True, blank=True)
    tags = TaggableManager()


    def __str__(self):
        return self.title
    
class Category(models.Model):
    category_name = models.CharField(max_length=255, default="หมวดหมู่ทั่วไป")
    category_detail = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.category_name
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    detail = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    images = models.ImageField(upload_to="products", null=True, blank=True)
    quantity = models.IntegerField(default=1)
    available = models.BooleanField(default=True)
    unit = models.CharField(max_length=255, default="-")
    image_url = models.CharField(max_length=255, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, max_length=180, null=True, blank=True)

    def __str__(self):
        return self.name

