from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
import uuid


class Stylist(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    joined_date = models.DateTimeField('date joined')
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.first_name


class Client(User):
    user = models.OneToOneField(User, parent_link=True, on_delete=models.CASCADE)
    #client_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    address = models.CharField(max_length=50, blank=True)
    zip_code = models.CharField(max_length=20, default='')
    city = models.CharField(max_length=25, blank=True)
    country = models.CharField(max_length=25, blank=True)
    location = models.CharField(max_length=25, blank=True)
    phone_number = models.CharField(validators=[RegexValidator(regex='^\+?[1-9]\d{1,14}$')], max_length=15, null=True)

    def __str__(self):
        return self.acc_test_fn + self.acc_test_ln

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
