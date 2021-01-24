from django.urls import path
from . import views


urlpatterns = [
    path('', views.memberships, name="memberships"),
    path('membership_checkout/', views.membership_checkout,
         name="membership_checkout"),
]
