from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# manage about register
from django.contrib.auth.models import User

# about authentication and login
from django.contrib.auth import authenticate, login, logout

from django.core.files.storage import FileSystemStorage

import string
import random
from datetime import datetime

def Home(req):
    if req.user.is_authenticated:
        first_name = req.user.first_name
        return HttpResponse(f"<h1>hello {first_name}</h1>")
    else:
        return HttpResponse(f"<h1>hello World</h1>")

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
                return redirect('home')
            except:
                context['wrongpassword'] = 'wrongpassword'

    return render(req, 'myapp/login.html', context)




def logout_view(req):
    logout(req)
    return render(req, 'myapp/login.html')


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


def randomOrderID():
    random_id = ""
    random_id += random.choice(string.ascii_uppercase)
    random_id += random.choice(string.ascii_uppercase)

    for i in range(8):
        random_id += random.choice("0123456789")


    return random_id

def ProductDetail(req, slug):

    randomOrderID()

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
        new_order.shipping_cost = product.shipping_cost * int(data.get('count'))


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

        

        # เพิ่ม function random id
        try:
            
            tracking_id = TrackingOrderID.objects.all()

            while True:
                order_ID = randomOrderID()
                for tid in tracking_id: # check if the tracking id is complicated.
                    if order_ID == tid.order_id:
                        continue
                break
        except:
            
            order_ID = randomOrderID()

        new_tracking_id = TrackingOrderID()
        new_tracking_id.tracking_order = new_order
        new_tracking_id.order_id = order_ID
        new_tracking_id.save()

        return redirect("tracking-order-page", order_ID)


    return render(req, "myapp/product-detail.html", context)



def TrackingOrderId(req, tid):

    tracking_id = TrackingOrderID.objects.get(order_id=tid).tracking_order
    buyer_price = tracking_id.buyer_price

    if buyer_price == int(buyer_price):
        buyer_price = int(buyer_price)


    shipping_cost = tracking_id.shipping_cost
    print('shipping cost',shipping_cost)
    if shipping_cost == int(shipping_cost):
        shipping_cost = int(shipping_cost)

    all_price = tracking_id.buyer_price + tracking_id.shipping_cost

    context = {
                    "tracking_id": tracking_id, 
                    "buyer_price": buyer_price, 
                    "order_id": tid,
                    "shipping_cost": shipping_cost, 
                    "all_price": all_price
               
               }
    
    return render(req, "myapp/tracking-order.html", context)

def AddToCart(req, pid):
    username = req.user.username
    user = User.objects.get(username=username)
    check = Product.objects.get(id=pid)

    try:
        new_cart = Cart.objects.get(user=user, product_id=str(pid))
        new_quantity = new_cart.quantity + 1
        new_cart.quantity = new_quantity
        calculate  = new_cart.price * new_quantity
        new_cart.total = calculate
        new_cart.save()

        count = Cart.objects.filter(user=user)
        count = sum([c.quantity for c in count])


        updated_quantity = Profile.objects.get(user=user)
        updated_quantity.cart_quantity = count
        updated_quantity.save()

        return redirect('all-product')
    
    except:
        new_cart = Cart()
        new_cart.user = user
        new_cart.product_id = pid
        new_cart.product_name = check.name
        new_cart.price = int(check.normal_price)
        new_cart.quantity = 1
        calculate  = new_cart.price * new_cart.quantity
        new_cart.total = calculate
        new_cart.save()

        count = Cart.objects.filter(user=user)
        count = sum([c.quantity for c in count])

        updated_quantity = Profile.objects.get(user=user)
        updated_quantity.cart_quantity = count
        updated_quantity.save()

        return redirect('all-product')


def MyCart(req):
    username = req.user.username
    user = User.objects.get(username=username)
    context = {}
    if req.method == "POST":
        data = req.POST.copy()
        product_id = data.get("product_id")
        try:
            item = Cart.objects.get(user=user, product_id=product_id)
            item.delete()
            context['status'] = 'delete'
        except Cart.DoesNotExist:
            item = None

        count = Cart.objects.filter(user=user)
        count = sum([c.quantity for c in count])
        updated_quantity = Profile.objects.get(user=user)
        updated_quantity.cart_quantity = count
        updated_quantity.save()
    mycart = Cart.objects.filter(user=user)
    count = sum([c.quantity for c in mycart])
    total = sum([c.total for c in mycart])

    context['mycart'] = mycart
    context['count']  = count
    context['total'] = total


    return render(req, "myapp/my-cart.html", context)


def MyCartEdit(req):
    username = req.user.username
    user = User.objects.get(username=username)

    if req.method == "POST":
        data = req.POST.copy()

        print(data)

        if data.get("clear") == "clear":
            Cart.objects.filter(user=user).delete()
            updated_quantity = Profile.objects.get(user=user)
            updated_quantity.cart_quantity = 0
            updated_quantity.save()

            return redirect("my-cart")
        
        edit_list = []
        for k, v in data.items():
            if k[:2] == "pd":
                pid = int(k.split("_")[1])
                dt = [pid, int(v)]
                edit_list.append(dt)

        for ed in edit_list:
            edit_cart = Cart.objects.get(product_id=ed[0], user=user)
            edit_cart.quantity = ed[1]
            calculate = edit_cart.price * ed[1]
            edit_cart.total = calculate
            edit_cart.save()

        count = Cart.objects.filter(user=user)
        count = sum([c.quantity for c in count])
        updated_quantity = Profile.objects.get(user=user)
        updated_quantity.cart_quantity = count
        updated_quantity.save()

        return redirect("my-cart")
    

    context = {}
    mycart = Cart.objects.filter(user=user)
    context["mycart"] = mycart

    return render(req, "myapp/my-cart-edit.html", context)

def Checkout(req):
    username = req.user.username
    user = User.objects.get(username=username)

    if req.method == "POST":
        data = req.POST.copy()


        first_name = data.get('first_name')
        last_name = data.get('last_name')
        tel = data.get('tel')
        email = data.get('email')
        address = data.get('address')
        express = data.get('express')
        payment = data.get('payment')
        other =data.get('other')
        page = data.get('page')

        if page == "information":
            context = {}
            context["first_name"] = first_name
            context["last_name"] = last_name
            context["tel"] = tel
            context["email"] = email
            context["address"] = address
            context["express"] = express
            context["payment"] = payment
            context["other"] = other
            

            mycart = Cart.objects.filter(user=user)
            count = sum([c.quantity for c in mycart])
            total = sum([c.total for c in mycart])


            context["mycart"] = mycart
            context["count"] = count
            context["total"] = total


            return render(req, "myapp/checkout-confirm.html", context)
        

        if page == "confirm":
            mycart = Cart.objects.filter(user=user)
            member_id = str(user.id).zfill(4)
            date_time = datetime.now().strftime("%Y%m%d%H%M%S")
            order_id = "OD" + member_id + date_time


            for mc in mycart:
                cart_order = OrderProduct()
                cart_order.order_id = order_id
                cart_order.product_id = mc.product_id
                cart_order.product_name = mc.product_name
                cart_order.price = mc.price
                cart_order.quantity = mc.quantity
                cart_order.total_price = mc.total
                cart_order.save()

            new_order = CartOrder()
            new_order.order_id = order_id
            new_order.user = user
            new_order.first_name = first_name
            new_order.last_name = last_name
            new_order.tel = tel
            new_order.email = email
            new_order.address = address
            new_order.express = express
            new_order.payment = payment
            new_order.other = other
            new_order.save()

            Cart.objects.filter(user=user).delete()
            update_quantity = Profile.objects.get(user=user)
            update_quantity.cart_quantity = 0
            update_quantity.save()

            return redirect('upload-slip-order', order_id=order_id)
        
    return render(req, 'myapp/checkout.html')

def CartOrderProduct(req):
    username = req.user.username
    user = User.objects.get(username=username)

    context = {}

    cart_order = CartOrder.objects.filter(user=user)

    for co in cart_order:
        order_id = co.order_id
        order_product = OrderProduct.objects.filter(order_id=order_id)
        total = sum([o.total_price for o in order_product])
        co.total_price = total
        count = sum([o.quantity for o in order_product])

        if co.express == "flash":
            shipping_cost = sum([20 if i == 0 else 10 for i in range(count)])
        elif co.express == "kerry":
            shipping_cost = sum([20 if i == 0 else 8 for i in range(count)])
        elif co.express == "jst":
            shipping_cost = sum([20 if i == 0 else 9 for i in range(count)])
        elif co.express == "thailandpost":
            shipping_cost = sum([20 if i == 0 else 12 for i in range(count)])
        else:
            shipping_cost = sum([20 if i == 0 else 11 for i in range(count)])

        if co.payment == "cod":
            shipping_cost += 10

        co.shipping_cost = shipping_cost


    context["cart_order"] = cart_order

    return render(req, "myapp/cart-order-product.html", context)

def UploadSlipOrder(req, order_id):
    if req.method == "POST" and req.FILES['upload_slip']:
        data = req.POST.copy()

        slip_time = data.get('slip_time')
        bank_account = data.get("bank_account")

        updated_cart_order = CartOrder.objects.get(order_id=order_id)
        updated_cart_order.slip_time = slip_time
        updated_cart_order.bank_account = bank_account

        file_image_slip = req.FILES['upload_slip']
        file_image_name = req.FILES['upload_slip'].name.replace(" ", "")
        file_system_storage = FileSystemStorage()
        file_name = file_system_storage.save(file_image_name, file_image_slip)
        upload_file_url = file_system_storage.url(file_name)
        updated_cart_order.slip = upload_file_url[6:]

        updated_cart_order.save()

    order_product = OrderProduct.objects.filter(order_id=order_id)
    total = sum([o.total_price for o in order_product])
    cart_order_detail = CartOrder.objects.get(order_id=order_id)
    count = sum([o.quantity for o in order_product])

    if cart_order_detail.express == 'flash':
        shipping_cost = sum([20 if i == 0 else 10 for i in range(count)])
    elif cart_order_detail.express == 'kerry':
        shipping_cost = sum([20 if i == 0 else 8 for i in range(count)])
    elif cart_order_detail == 'jst':
        shipping_cost = sum([20 if i == 0 else 9 for i in range(count)])
    elif cart_order_detail.express == 'thailandpost':
        shipping_cost = sum([20 if i == 0 else 12 for i in range(count)])
    else:
        shipping_cost = sum([20 if i == 0 else 11 for i in range(count)])


    if cart_order_detail.payment == 'cod':
        shipping_cost += 10

    context = {"order_id": order_id, 
               "total": total, 
               "shipping_cost": shipping_cost,
               "grand_total": total + shipping_cost,
               "cart_order_detail": cart_order_detail,
               "count": count
               }

    return render(req, "myapp/upload-slip-order.html", context)

def CustomerAllOrder(req):
    context = {}
    cart_order = CartOrder.objects.all().order_by("-id") # reverse order by plus "-"
    for co in cart_order:
        order_id = co.order_id
        order_product = OrderProduct.objects.filter(order_id=order_id)
        total = sum([o.total_price for o in order_product])
        co.total_price = total
        count = sum([o.quantity for o in order_product])

        if co.express == 'flash':
            shipping_cost = sum([20 if i == 0 else 10 for i in range(count)])
        elif co.express == 'kerry':
            shipping_cost = sum([20 if i == 0 else 8 for i in range(count)])
        elif co == 'jst':
            shipping_cost = sum([20 if i == 0 else 9 for i in range(count)])
        elif co.express == 'thailandpost':
            shipping_cost = sum([20 if i == 0 else 12 for i in range(count)])
        else:
            shipping_cost = sum([20 if i == 0 else 11 for i in range(count)])

        if co.express == "cod":
            shipping_cost += 10

        co.shipping_cost = shipping_cost


    context["cart_order"] = cart_order
    return render(req, "myapp/customer-all-order.html", context)


def UpdatePaid(req, order_id, status):
    try:
        if req.user.profile.usertype != 'admin':
            return redirect("home")
        
    except:
        return render('all-product')
    
    cart_order = CartOrder.objects.get(order_id=order_id)
    if status == "confirm":
        cart_order.paid = True
        cart_order.confirmed = True
        order_product = OrderProduct.objects.filter(order_id=order_id)

        for op in order_product:
            product = Product.objects.get(id=op.product_id)
            product.quantity = product.quantity - op.quantity
            product.save()
    elif status == "cancel":
        cart_order.paid = False
        cart_order.confirmed = False
    cart_order.save()

    return redirect("customer-all-order")


def CartOrderUpdateTracking(req, order_id):
    # try:
    #     if req.user.profile.usertype != 'admin':
    #         return redirect("home")
        
    # except:
    #     return render('all-product')
    
    if req.method == 'POST':
        cart_order = CartOrder.objects.get(order_id=order_id)
        data = req.POST.copy()

        tracking_number = data.get('tracking_number')
        cart_order.tracking_number = tracking_number
        cart_order.save()

        return redirect("customer-all-order")

    cart_order = CartOrder.objects.get(order_id=order_id)
    order_product = OrderProduct.objects.filter(order_id=order_id)



    total = sum([o.total_price for o in order_product])
    cart_order.total_price = total
    count = sum([o.quantity for o in order_product])


    if cart_order.express == 'flash':
        shipping_cost = sum([20 if i == 0 else 10 for i in range(count)])
    elif cart_order.express == 'kerry':
        shipping_cost = sum([20 if i == 0 else 8 for i in range(count)])
    elif cart_order == 'jst':
        shipping_cost = sum([20 if i == 0 else 9 for i in range(count)])
    elif cart_order.express == 'thailandpost':
        shipping_cost = sum([20 if i == 0 else 12 for i in range(count)])
    else:
        shipping_cost = sum([20 if i == 0 else 11 for i in range(count)])

    if cart_order.express == "cod":
        shipping_cost += 10
    cart_order.shipping_cost = shipping_cost

    context = {"cart_order": cart_order, 
               "order_product": order_product,
               "total": total, 
               "count": count,
               }

    return render(req, "myapp/cart-order-update-tracking.html", context)

def MyOrder(req, order_id):
    username = req.user.username
    user = User.objects.get(username=username)

    cart_order = CartOrder.objects.get(order_id=order_id)
    if user != cart_order.user:
        return redirect('all-product')
    
    order_product = OrderProduct.objects.filter(order_id=order_id)

    total = sum([o.total_price for o in order_product])
    cart_order.total_price = total
    count = sum([o.quantity for o in order_product])


    if cart_order.express == 'flash':
        shipping_cost = sum([20 if i == 0 else 10 for i in range(count)])
    elif cart_order.express == 'kerry':
        shipping_cost = sum([20 if i == 0 else 8 for i in range(count)])
    elif cart_order == 'jst':
        shipping_cost = sum([20 if i == 0 else 9 for i in range(count)])
    elif cart_order.express == 'thailandpost':
        shipping_cost = sum([20 if i == 0 else 12 for i in range(count)])
    else:
        shipping_cost = sum([20 if i == 0 else 11 for i in range(count)])

    if cart_order.express == "cod":
        shipping_cost += 10
    cart_order.shipping_cost = shipping_cost

    context = {"cart_order": cart_order,
               "order_product": order_product,
               "total": total,
               "count": count,
               }
    
    return render(req, "myapp/my-order.html", context)

def AllMachine (req):

    machines = Machine.objects.filter(available=True)
    context = {"machines": machines}

    return render(req, "myapp/machines.html", context)

def MachineDetail(req, machine_id):

    machines = Machine.objects.all().order_by("id").reverse()[:6]
    machine = get_object_or_404(Machine, id=machine_id)
    comments = Comments.objects.filter(machine=machine, parent=None)

    username = req.user.username
    user = User.objects.get(username=username)

    if req.method == "POST":
        data = req.POST.copy()

        content = data.get("content")
        name = data.get("name")
        email = data.get("email")
        website = data.get("website")
        parent_id = data.get("parent")


        parent_obj = None
        
        if content:
            if parent_id:
                parent_obj = Comments.objects.get(id=parent_id)
                comment_reply = Comments(
                    author=user,
                    content=content,
                    parent=parent_obj,
                    machine=machine,
                    name=name,
                    email=email,
                    website=website,
                )

                comment_reply.save()

                return HttpResponseRedirect(
                    reverse("machine-detail-page", kwargs={"machine_id": machine_id})
                )

            else:
                comment = Comments(
                    author=user,
                    content=content,
                    machine=machine,
                    name=name,
                    email=email,
                    website=website,
                )

                comment.save()

                return HttpResponseRedirect(
                    reverse("machine-detail-page", kwargs={"machine_id": machine_id})
                )
            

    context = {"machines": machines, "comments": comments, "machine": machine}

    return render(req, "myapp/machine-detail.html", context)



    
