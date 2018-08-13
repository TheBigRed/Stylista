from django.db import models
from landing.models import Stylist


class Review(models.Model):
    client = models.ForeignKey(Stylist, models.CASCADE, related_name='client_review')
    stylist = models.ForeignKey(Stylist, models.CASCADE, related_name='stylist_review')
    confirmed_client = models.BooleanField(default=None, blank=True)
    title = models.CharField(max_length=25, blank=True)
    review = models.TextField(blank=True)
    rating = models.FloatField(blank=True)
    date = models.DateField()
    time = models.TimeField()
    helpful_count = models.IntegerField(default=0, blank=True)
    unhelpful_count = models.IntegerField(default=0, blank=True)
    helpful_total_count = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.title
