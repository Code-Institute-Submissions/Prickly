from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name="cart"),
    path('<product_id>/add/',
         views.add_item_to_cart,
         name="add_item_to_cart"),
]
