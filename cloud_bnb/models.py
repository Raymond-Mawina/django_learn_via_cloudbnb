from django.db import models
from taggit.managers import TaggableManager


class Picture(models.Model):
    name = models.TextField(max_length=100)
    isFavorite = models.BooleanField()


class Property(models.Model):
    description = models.CharField(max_length=255)
    pictures = models.ForeignKey(to=Picture, on_delete=models.PROTECT)
    city = models.CharField(max_length=100)
    suburb = models.CharField(max_length=100)
    street_address = models.CharField(max_length=100)
    max_num_of_guests = models.IntegerField()
    price_per_night_for_one_guest = models.IntegerField()
    price_per_night_per_extra_guest = models.IntegerField()
    tags = TaggableManager()
