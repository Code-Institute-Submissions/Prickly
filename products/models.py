#  import ColorField for Color.color_hex
from colorfield.fields import ColorField
from django.db import models


# Creating categories model
class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=20)
    color_hex = ColorField(default='#FFFFFF')

    def __str__(self):
        return self.name


# Creating a products table
class Product(models.Model):
    # overriding the products_product table name
    class Meta:
        db_table = 'products'

    product_code = models.CharField(max_length=20, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    avg_rating = models.DecimalField('average product rating', max_digits=2,
                                     decimal_places=1, default=0,
                                     null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    many_colors = models.BooleanField(default=False)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL,
                              null=True, blank=True)
    main_pic = models.ImageField('thumbnail picture', null=True, blank=True)
    pic2 = models.ImageField(null=True, blank=True)
    pic3 = models.ImageField(null=True, blank=True)
    pic4 = models.ImageField(null=True, blank=True)
    added_date = models.DateTimeField(auto_now_add=True)
    release_date = models.DateTimeField('product release date',
                                        help_text="""Select today/now as the input
                                                  if the product is being
                                                  published now.""")

    def __str__(self):
        return self.name

    # Returns days/hours until the product release if release date is in future
    def release_countdown(self):
        pass
