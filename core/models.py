from django.db import models
from landing.models import Stylist


class Account(models.Model):
    account_holder = models.ForeignKey(Stylist, models.CASCADE, related_name='account')
    stylist_type = models.CharField(max_length=25, blank=True)
    location = models.CharField(max_length=25, blank=True)

    def __str__(self):
        return self.account_holder
