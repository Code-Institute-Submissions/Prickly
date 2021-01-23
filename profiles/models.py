from django.db import models
from django_countries.fields import CountryField
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

from memberships.models import Membership
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Creates a user profile model containing user's
    delivery details, order history and membership type
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    membership = models.ForeignKey(Membership, on_delete=models.CASCADE)
    user_phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                      message="Enter phone number in a format:"
                                      "'+111111111' and no longer that "
                                      "15 digits.")
    user_phone_number = models.CharField(validators=[user_phone_regex],
                                         max_length=16, null=True,
                                         blank=True)
    user_email = models.EmailField(max_length=254, null=True, blank=True)
    user_address_line_1 = models.CharField(max_length=100, null=True,
                                           blank=True)
    user_address_line_2 = models.CharField(max_length=100, null=True,
                                           blank=True)
    user_city = models.CharField('city or town', max_length=85, null=True,
                                 blank=True)
    user_region = models.CharField('region or county', max_length=85,
                                   null=True, blank=True)
    user_country = CountryField(blank_label='Country *',
                                null=True, blank=True)
    user_postcode = models.CharField('post/zip code', max_length=10,
                                     null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def update_or_create_profile(sender, instance, created, **kwargs):
    """
    If user doesn't have a profile yet, create it,
    otherwise update it
    """
    if created:
        Profile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
