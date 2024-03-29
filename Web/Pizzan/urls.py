from django.urls import path
from . import views
app_name = "Pizzan"
urlpatterns = [
    path("", views.home, name="home"),
    path("shop/", views.shop, name="shop"),
    path("shop-details/<int:id>/", views.shop_details, name="shop-details"),
    path("cart/", views.cart, name="cart"),
    path("checkout/", views.checkout, name="checkout"),
]