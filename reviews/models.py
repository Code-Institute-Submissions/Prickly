from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from profiles.models import Profile
from products.models import Product


class Review(models.Model):
    """
    Creates a review model to allow user to perform
    CRUD operations on product reviews
    """
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1),
                                             MaxValueValidator(5)],
                                 default=1)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
