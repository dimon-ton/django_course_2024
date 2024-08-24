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
    # Cart
    path("add-to-cart/<int:pid>/", AddToCart, name="add-to-cart"),
    path("cart", MyCart, name="my-cart"),
    path("edit-cart", MyCartEdit, name="my-cart-edit"),
    path("checkout", Checkout, name="checkout"),
    path("orders", CartOrderProduct, name="cart-order-product"),
    path("upload-slip/<str:order_id>/", UploadSlipOrder , name="upload-slip-order"),
    path("customer-all-order", CustomerAllOrder , name="customer-all-order"),
    path("update-status/<str:order_id>/<str:status>", UpdatePaid, name="update-status"),
    path("update-tracking/<str:order_id>/", CartOrderUpdateTracking, name="cart-order-update-tracking"),
    path("my-order/<str:order_id>/", MyOrder, name="my-order"),
]
