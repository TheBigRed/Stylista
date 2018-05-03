from django.db import models
from landing.models import Stylist


class Account(models.Model):
    account_holder = models.ForeignKey(Stylist, models.CASCADE, related_name='account_holder')
    stylist_type = models.CharField(max_length=25)
    location = models.CharField(max_length=25)

    def __str__(self):
        return self.first_name
