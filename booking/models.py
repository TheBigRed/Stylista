from django.db import models


class Contract(models.Model):
    client = models.ForeignKey(Stylist, models.CASCADE, related_name='client')
    stylist = models.ForeignKey(Stylist, models.CASCADE, related_name='stylist')
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=25, blank=True)
    total_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
