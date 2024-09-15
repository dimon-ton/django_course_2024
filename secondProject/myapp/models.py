from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

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
    introduction = models.TextField(null=True, blank=True)
    detail = models.TextField(null=True, blank=True)
    normal_price = models.IntegerField(null=True, blank=True)
    price1 = models.IntegerField(null=True, blank=True)
    price2 = models.IntegerField(null=True, blank=True)
    shipping_cost = models.FloatField(default=40, null=True, blank=True)
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
    


class Order(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    tel = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    address = models.TextField()
    count = models.IntegerField(default=1)
    buyer_price = models.FloatField(default=0)
    shipping_cost = models.FloatField(default=0)
    slip = models.ImageField(upload_to="product-slip/")
    # เพิ่มใหม่
    tracking_number = models.CharField(max_length=100, null=True, blank=True)
    not_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name
        


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.CharField(max_length=100, null=True, blank=True)
    product_name = models.CharField(max_length=100, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    stamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    total = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return self.product_name


# สร้าง class Tracking Order
class TrackingOrderID(models.Model):
    tracking_order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_id")
    order_id = models.CharField(max_length=10)

    def __str__(self):
        return self.order_id




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile_photo', null=True, blank=True)
    usertype = models.CharField(max_length=100, default='member')
    favor = models.CharField(max_length=100, null=True, blank=True)
    fb_account = models.CharField(max_length=100, default='No Facebook')
    address = models.TextField(null=True, blank=True)
    telephone_number = models.CharField(max_length=8, null=True, blank=True)
    # เพิ่มใหม่
    cart_quantity = models.IntegerField(default=0, null=True, blank=True)


    def __str__(self):
        return self.user.username

class OrderProduct(models.Model):
    order_id = models.CharField(max_length=100, null=True, blank=True)
    product_id = models.CharField(max_length=100, null=True, blank=True)
    product_name = models.CharField(max_length=100, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    total_price = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.product_name
    

class CartOrder(models.Model):
    order_id = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    tel = models.CharField(max_length=14, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    address = models.TextField()
    express = models.CharField(max_length=100)
    payment = models.CharField(max_length=100)
    other = models.TextField(null=True, blank=True)
    stamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    paid = models.BooleanField(default=False)
    confirmed = models.BooleanField(default=False)
    slip = models.ImageField(upload_to="cart-slip/", null=True, blank=True)
    slip_time = models.DateField(null=True, blank=True)
    bank_account = models.CharField(
        max_length=100,
        choices=[('kbank', 'kbank'), 
                 ('scb', 'scb'), 
                 ('tmb', 'tmb'), 
                 ('bbl', 'bbl'), 
                 ('kbank', 'kbank'),
                 ('อื่น ๆ', 'อื่น ๆ'),
                 ],

         default='kbank'        
        )
    
    payment_id = models.CharField(max_length=100, null=True, blank=True)
    tracking_number = models.CharField(max_length=100, null=True, blank=True)
    total_price = models.IntegerField(null=True, blank=True)
    shipping_cost = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return self.order_id
    
class Discount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    percent = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    active = models.BooleanField(default=False)


class Machine(models.Model):

    MACHINE_TYPE = [
        ("cnc", "CNC"),
        ("lathe", "เครื่องกลึง"),
        ("milling", "เครื่องกัด"),
        ("gear milling", "เครื่องไสเฟือง"),
    ]

    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.CharField(max_length=4)
    machine_type = models.CharField(max_length=100, choices=MACHINE_TYPE, default="CNC")
    images = models.ImageField(upload_to="machines", null=True, blank=True)
    price_per_day = models.IntegerField(default=0)
    earnest_money = models.IntegerField(default=10000, null=True, blank=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Reservation(models.Model):

    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    id_card = models.CharField(max_length=13)
    customer_name = models.CharField(max_length=50)
    tel = models.CharField(max_length=11)
    email = models.CharField(max_length=50, null=True, blank=True)
    rental_price = models.IntegerField(default=0)
    total_rental_price = models.ImageField(default=0)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.customer_name
    

class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    website = models.CharField(max_length=50)
    parent = models.ForeignKey("self", on_delete=models.DO_NOTHING, null=True, blank=True, related_name="replies")








