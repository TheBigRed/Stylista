from django.db import models
from landing.models import Stylist, Stylista


class UserSetting(models.Model):
    account_holder = models.ForeignKey(Stylist, models.CASCADE, related_name='settings_account')
    notifications = models.BooleanField()
    push_notifications = models.BooleanField()
    text_notifications = models.BooleanField()
    promotions = models.BooleanField()
    search_engine = models.BooleanField()
    deactivate = models.BooleanField()
    time_zone = models.CharField(max_length=15)
    languages = models.CharField(max_length=15)
    currency = models.CharField(max_length=15)

    def __str__(self):
        return self


class Service(models.Model):
    user = models.OneToOneField(Stylista, models.CASCADE)
    service_name = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=50, blank=True)
    duration = models.DurationField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True)