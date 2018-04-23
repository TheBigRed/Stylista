from django.db import models


class Stylist(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    joined_date = models.DateTimeField('date joined')
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.first_name
