from django.urls import path
from .views import *

urlpatterns = [
    path('', Home, name='home'),
    path("shop", myShop, name='shop'),
    path("aboutus", aboutUs, name='about-us'),
    path("contactus", contactUs, name='contact'),
    path("tracking", tracking, name='tracking'),
    path("satisfy", satisfy, name='satisfy'),
    path("ask", ask, name="ask"),
    path("questions", question, name="questions"),
    path("anwser/<int:askid>", anwser, name="answer"),
    path("blogs", PostPage, name="post"),
    path("blog-detail/<slug:slug>/", postDetail, name="blog-detail"),
    # register and login page  
    path("register", register, name="register"),
    path("login", Login, name="login"),
    path("logout",logout_view, name="logout"),
    path("products", AllProduct, name="all-product"),
    path("discount", DiscountPage, name="discount"),
    path("product/<slug:slug>", ProductDetail, name="product-detail"),
    path("tracking-order/<str:tid>/", TrackingOrderId, name="tracking-order-page"),
]
