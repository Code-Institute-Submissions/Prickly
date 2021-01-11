#  import ColorField for Color.color_hex
from colorfield.fields import ColorField
from django.db import models


# Creating categories model
class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=20)

    # Change string representation of the object
    def __str__(self):
        return self.name


# Creating a products table
class Product(models.Model):
    YES = 'Y'
    NO = 'N'
    MANY_COLORS = [
        (YES, 'Yes'),
        (NO, 'No'),
    ]

    product_code = models.CharField(max_length=20, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    avg_rating = models.DecimalField('average product rating', max_digits=2,
                                     decimal_places=1, default=0,
                                     null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    many_colors = models.CharField(max_length=1,
                                   choices=MANY_COLORS,
                                   help_text=('Will the product come in '
                                              'multiple colors?'))
    main_pic = models.ImageField('thumbnail picture', null=True, blank=True)
    pic2 = models.ImageField('additional picture 2', null=True, blank=True)
    pic3 = models.ImageField('additional picture 3', null=True, blank=True)
    pic4 = models.ImageField('additional picture 4', null=True, blank=True)
    added_date = models.DateTimeField(auto_now_add=True)
    release_date = models.DateTimeField('product release date',
                                        help_text=('Select today/now as the '
                                                   'inout if the product is '
                                                   'being published now.'))

    def __str__(self):
        return self.name

    # Returns days/hours until the product release if release date is in future
    def release_countdown(self):
        pass


class Color(models.Model):
    name = models.CharField(max_length=20)
    color_hex = ColorField(default='#FFFFFF')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                null=True, blank=True)

    def __str__(self):
        return self.name
