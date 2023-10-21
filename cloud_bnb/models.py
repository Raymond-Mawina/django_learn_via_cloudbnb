from django.db import models


class Property(models.Model):
    description = ""
    pictures = ""
    city = ""
    suburb = ""
    street_address = ""
    max_num_of_guests = ""
    price_per_night_for_one_guest = ""
    price_per_night_per_extra_guest = ""
    tags = ""
