from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from products.models import Flowers

from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    User profile model to maintain default
    delivery information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(
        max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(
        max_length=100, null=True, blank=True)
    default_street_address2 = models.CharField(
        max_length=100, null=True, blank=True)
    default_postcode = models.CharField(
        max_length=20, null=True, blank=True)
    default_town_or_city = models.CharField(
        max_length=50, null=True, blank=True)
    default_county = models.CharField(
        max_length=100, null=True, blank=True)
    default_country = CountryField(
        blank_label='Country', null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """ Creates or updates user profile """
    if created:
        UserProfile.objects.create(user=instance)
    # For existing users, saves the profile
    instance.userprofile.save()


class FavoriteList(models.Model):
    """ Model for a users favorites """

    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    products = models.ManyToManyField(Flowers, blank=True)

    @property
    def qty_favorite_items(self):
        return self.products.count()
