import uuid

from django.db import models
from django.core.validators import RegexValidator

from products.models import Product

from django_countries.fields import CountryField


class Order(models.Model):
    STANDARD = 'S'
    EXPRESS = 'E'
    DELIVERY_TYPE = [
        (STANDARD, 'Standard'),
        (EXPRESS, 'Express'),
    ]

    order_number = models.CharField(max_length=36, default=uuid.uuid4,
                                    editable=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    full_name = models.CharField(max_length=70, editable=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Enter phone number in a format: "
                                         "'+111111111' and no longer that "
                                         "15 digits.")
    phone_number = models.CharField(validators=[phone_regex], max_length=18,
                                    blank=True)
    email = models.EmailField(max_length=254)
    address_line_1 = models.CharField(max_length=100,)
    address_line_2 = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField('city or town', max_length=85)
    region = models.CharField('region or county', max_length=85, null=True,
                              blank=True)
    country = models.CountryField(blank_label='Country *')
    postcode = models.CharField('post/zip code', max_length=10)
    order_date = models.DateTimeField(auto_now_add=True)
    dispatch_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    delivery_type = models.CharField(max_length=1, choices=DELIVERY_TYPE)
    delivery_cost = models.DecimalField(max_digits=7, decimal_places=2,
                                        default=0)
    subtotal = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=7, decimal_places=2, default=0)

    class OrderLine(models.Model):

        order_id = models.ForeignKey(Order, on_delate=models.CASCADE)
        product = models.ForeignKey(Product, on_delate=models.CASCADE)
        color = models.CharField(max_length=20, null=True, blank=True)
        quantity = models.IntegerField(default=0)
        line_total = models.DecimalField(max_digits=7, decimal_places=2,
                                         default=0, editable=False)
