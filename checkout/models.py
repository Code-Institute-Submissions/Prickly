import uuid

from decimal import Decimal

from django.db import models
from django.db.models import Sum
from django.core.validators import RegexValidator

from django_countries.fields import CountryField

from products.models import Product


class DeliveryType(models.Model):
    """
    Creates Delivery Type Model containing specific
    data on each specific dleivery type
    """
    name = models.CharField('Delivery Type', max_length=20)
    dispatch_speed = models.IntegerField('days to dispatch order')
    delivery_speed = models.IntegerField('days to deliver order')
    limit = models.DecimalField('order amount limit for set delivery cost',
                                max_digits=5, decimal_places=2, default=0)
    const = models.DecimalField('set delivey cost', max_digits=5,
                                decimal_places=2, default=0)
    rate = models.DecimalField('delivery rate', max_digits=5,
                               decimal_places=2, default=0)

    def __str__(self):
        return self.name


class Order(models.Model):
    """
    Creates Order Model containing data on each order
    which also potentially contains multiple products
    """
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
    country = CountryField(blank_label='Country *')
    postcode = models.CharField('post/zip code', max_length=10)
    order_date = models.DateTimeField(auto_now_add=True)
    dispatch_date = models.DateTimeField('order dispatched on',
                                         null=True, blank=True)
    est_dispatch_dte = models.DateTimeField('estimated order dispatch date',
                                            editable=False)
    delivery_date = models.DateTimeField('order delivered on',
                                         null=True, blank=True)
    est_deliery_dte = models.DateTimeField('estimated order delivery date',
                                           editable=False)
    delivery_type = models.ForeignKey(DeliveryType, on_delete=models.CASCADE)
    delivery_cost = models.DecimalField(max_digits=7, decimal_places=2,
                                        default=0)
    subtotal = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=7, decimal_places=2, default=0)

    def total_amount(self):
        """
        Calculate the subtotal, delivery cost and the total,
        depending on the delivery type selected and products
        in the order
        """
        self.subtotal = self.order_line.aggregate(
            Sum('line_total'))['line_total__sum'] or 0

        if self.subtotal < self.delivery_type.limit:
            self.delivery_cost = self.delivery_type.const
        else:
            self.delivery_cost = self.subtotal * Decimal(
                self.delivery_type.rate / 100)
        self.total = self.subtotal + self.delivery_cost
        self.save()

    def estimate_order_dates(self):
        """
        Calculate estimated order processing dates
        """
        self.est_dispatch_dte = (self.order_date
                                 + self.delivery_type.dispatch_speed)
        self.est_deliery_dte = (self.order_date
                                + self.delivery_type.delivery_speed)
        self.save()

    def save(self, *args, **kwargs):
        """
        Make order number uppercase before save
        """
        self.order_number = self.order_number.upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLine(models.Model):
    """
    Creates OrderLine Model containing data on each product
    added to the cart
    """
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE,
                                 related_name='order_line')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.CharField(max_length=20, null=True, blank=True)
    quantity = models.IntegerField(default=0)
    line_total = models.DecimalField(max_digits=7, decimal_places=2,
                                     default=0, editable=False)

    def save(self, *args, **kwargs):
        """
        Calculate the total of a line item before saving
        an entry
        """
        self.line_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        """
        String Represention of the object
        """
        return f'{self.product.name} in order {self.order.order_number}'
