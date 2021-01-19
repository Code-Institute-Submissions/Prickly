from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name="checkout"),
    path('<order_number>/checkout_success/',
         views.checkout_success,
         name="checkout_success"),
]
