from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required

# manage about register
from django.contrib.auth.models import User

# about authentication and login
from django.contrib.auth import authenticate, login, logout

from django.core.files.storage import FileSystemStorage


def Home(req):
    return HttpResponse("<h1>hello world</h1>")


def myShop(req):
    return render(req, "myapp/home.html")

def aboutUs(req):
    return render(req, 'myapp/aboutus.html')

def contactUs(req):
    return render(req, 'myapp/contactus.html')

def tracking(req):
    # track_list = ['ลุงวิศวกร - A1234',
    #               'สมหญิง - A1235',
    #               'สมชาย - A1236'
    #               ]

    Tracking_list = Tracking.objects.all()
    print(Tracking_list)
    context = {'tracking':Tracking_list}

    return render(req, "myapp/tracking.html", context)

def ask(req):
    if req.method == 'POST':
        data = req.POST.copy()
        # print('data', data)
        name = data.get('name')
        email = data.get('email')
        title = data.get('title')
        detail = data.get('detail')


        QA_data = AskQA()
        QA_data.name = name
        QA_data.email = email
        QA_data.title = title 
        QA_data.detail = detail

        QA_data.save()



    return render(req, 'myapp/ask.html')


@login_required
def question(req):
    # track_list = ['ลุงวิศวกร - A1234',
    #               'สมหญิง - A1235',
    #               'สมชาย - A1236'
    #               ]

    question = AskQA.objects.all()
    print(question)
    context = {'question':question}

    return render(req, "myapp/questions.html", context)



def satisfy(req):

    data = [
            {
                'main': "ประสบการณ์การใช้งาน (User Experience)",
                'subtopics': [
                "ความสะดวกในการนำทางในเว็บไซต์",
                "ความรวดเร็วของเว็บไซต์",
                "ความเข้าใจในการใช้งานระบบ",
                "การแสดงผลข้อมูลและสินค้า"
                ]
            },
            {
                'main': "การให้บริการ (Customer Service)",
                'subtopics': [
                "การตอบรับและแก้ไขปัญหาของลูกค้า",
                "ความชัดเจนในการติดต่อและสื่อสาร",
                "ความเป็นมืออาชีพของทีมบริการลูกค้า"
                ]
            },
            {
                'main': "คุณภาพของข้อมูลและสารสนเทศ",
                'subtopics': [
                "ความถูกต้องและความครบถ้วนของข้อมูล",
                "ความชัดเจนในการแสดงข้อมูล",
                "ความทันสมัยของข้อมูล"
                ]
            },
            {
                'main': "ความปลอดภัยและความเป็นส่วนตัว",
                'subtopics': [
                "ระบบการรักษาความปลอดภัยของข้อมูลลูกค้า",
                "การสื่อสารที่เป็นส่วนตัวและความเปิดเผยที่เหมาะสม"
                ]
            },
            {
                'main': "ความพึงพอใจทั่วไป",
                'subtopics': [
                "ความพึงพอใจในบริการรวมถึงประสบการณ์ทั้งหมด",
                "ความพึงพอใจในการจัดส่งหรือการให้บริการพิเศษ",
                "ความพึงพอใจในราคาและสิ่งที่ได้รับ"
                ]
            }
            ]
    

    context = {'questionair':data}

    if req.method == 'POST':
        sex = req.POST.get('sex')
        age = req.POST.get('age')
        education = req.POST.get('education')
        offer = req.POST.get('offer')

        # Process radio button responses
        for q in context["questionair"]:
            for s in q["subtopics"]:
                item_name = f'item{context["questionair"].index(q) + 1}_{q["subtopics"].index(s) + 1}'
                response_value = req.POST.get(item_name)
                
                # Assuming you have a model named SurveyResponse
                SurveyResponse.objects.create(
                    sex=sex,
                    age=age,
                    education=education,
                    offer=offer,
                    question_main=q["main"],
                    question_subtopic=s,
                    response_value=response_value
                )      


    

    return render(req, "myapp/satisfy.html", context)


@login_required
def anwser(req, askid):
    # localhost:8000/answer/askid

    record = AskQA.objects.get(id=askid)

    if req.method == 'POST':
        data = req.POST.copy()

        # name = data.get('askid')
        detail_answer = data.get('detail_answer')

        record.detail_answer = detail_answer
        record.save()

    context = {'record': record}

    

    return render(req, 'myapp/anwser.html', context)



def PostPage(req):
    posts = Post.objects.all().order_by('id').reverse()[:3]

    context = {"posts":posts}

    return render(req, 'myapp/blogs.html', context)


def postDetail(req, slug):
    posts = Post.objects.all().order_by('id').reverse()[:3]

    try:
        single_post = get_object_or_404(Post, slug=slug)
        
    except Post.DoesNotExist:
        return render(req, 'myapp/home.html')
    

    context = {'single_post': single_post, "posts":posts}

    return render(req, 'myapp/blog-detail.html', context)



def register(req):

    context = {}

    if req.method == 'POST':
        data = req.POST.copy()

        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        check = User.objects.filter(username=email)


        if len(check) == 0:
            firstname, lastname = name.split(' ')

            newuser = User()
            newuser.username = email
            newuser.first_name = firstname
            newuser.last_name = lastname




            # password is different
            newuser.set_password(password)

            newuser.save()

            profile = Profile()
            profile.user = newuser
            profile.save()



            context['success'] = 'success'
        else:
            context['usertaken'] = 'usertaken'


    return render(req, 'myapp/register.html', context)


def Login(req):

    context = {}

    if req.method == 'POST':
        data = req.POST.copy()

        # name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        check = User.objects.filter(username=email)


        if len(check) == 0:

            context['nouser'] = 'nouser'
        else:
            try:
                user = authenticate(username=email,password=password)
                login(req, user)
                print("login complete")
                return redirect('shop')
            except:
                context['wrongpassword'] = 'wrongpassword'

    return render(req, 'myapp/login.html', context)




def logout_view(req):
    logout(req)
    return render(req, 'myapp/logout.html')


def AllProduct(req):
    all_product = Product.objects.filter(available=True)

    print(all_product)
    context = {"all_product":all_product}

    return render(req, "myapp/all-product.html", context)


def DiscountPage(req):

    context = {}

    if req.method == 'POST':
        data = req.POST.copy()

        check = data.get('discount')

        if check == 'check-true':
            # req.user.discount.active = True
            user = User.objects.get(username=req.user.username)

            discount = Discount.objects.get(user=user)
            discount.active = True
            discount.save()

            return redirect('all-product')


 


    return render(req, 'myapp/discount.html', context)


def ProductDetail(req, slug):
    product = Product.objects.get(slug=slug)

    context = {"product": product, "product_price": product.normal_price}

    if product.price1 > 0:
        price_1 = (product.price1 * 100) / product.normal_price

        context["price_1"] = 100 - int(price_1)
        context["product_price"] = product.price1


    if product.price2 > 0:
        price_2 = (product.price2 * 100) / product.normal_price

        context["price_2"] = 100 - int(price_2)

    if req.method == 'POST':
        data = req.POST.copy()

        new_order = Order()
        new_order.products = product
        new_order.first_name = data.get('first_name')
        new_order.last_name = data.get('last_name')
        new_order.tel = data.get('tel')
        new_order.email = data.get('email')
        new_order.address = data.get('address')
        new_order.count = data.get('count')
        new_order.buyer_price = data.get('buyer_price')
        new_order.shipping_cost = product.shipping_cost * data.get('count')


        # insert picture into the database

        try:
            file_image = req.FILES["upload_slip"]
            file_image_name = req.FILES["upload_slip"].name.replace(" ","")
            file_system_storage = FileSystemStorage()
            file_name = file_system_storage.save("product-slip/" + file_image_name, file_image)
            upload_file_url = file_system_storage.url(file_name)
            new_order.slip = upload_file_url[6:]

        except:

            new_order.slip = "/default.png"
        
        
        new_order.save()

    return render(req, "myapp/product-detail.html", context)