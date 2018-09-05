from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.contrib.postgres.fields import JSONField
import uuid, json


class Stylist(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    joined_date = models.DateTimeField('date joined')
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.first_name


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=50, blank=True)
    zip_code = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=25, blank=True)
    country = models.CharField(max_length=25, blank=True)
    location = models.CharField(max_length=25, blank=True)
    phone_number = models.CharField(validators=[RegexValidator(regex='^\+?[1-9]\d{1,14}$')],
                                    null=True, blank=True, max_length=15)

    def __str__(self):
        return self.user.first_name + self.user.last_name

    @receiver(post_save, sender=User)
    def create_client(sender, instance, **kwargs):
        print("Received post_save signal from User to create Stylista")

        if kwargs.get('created', False):
            Client.objects.update_or_create(user=instance)
            print("Client Created")

        else:
            print("Stylista not created")

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'


class Stylista(models.Model):

    STYLISTA_TYPES = (
        ('BARBER', 'Barber'),
        ('HAIR_STYLIST', 'Hair Stylist'),
        ('MAKEUP', 'Makeup Artist'),
        ('MUAH', 'Make Up And Hair'),
        ('NAILS', 'Nail Technician'),
        ('CLIENT', 'Client'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    business_id = models.UUIDField(default=uuid.uuid4, editable=False)
    stylist_type = models.CharField(max_length=25, choices=STYLISTA_TYPES, blank=True)
    about_me = models.TextField(blank=True)
    business_name = models.CharField(max_length=20, blank=True)
    services = JSONField(blank=True, null=True)
    address = models.CharField(max_length=50, blank=True)
    business_address = models.CharField(max_length=50, blank=True)
    zip_code = models.CharField(max_length=8, blank=True)
    business_zip_code = models.CharField(max_length=8, blank=True)
    city = models.CharField(max_length=15, blank=True)
    business_city = models.CharField(max_length=25, blank=True)
    country = models.CharField(max_length=15, blank=True)
    business_country = models.CharField(max_length=25, blank=True)
    business_location = models.CharField(max_length=25, blank=True)
    phone_number = models.CharField(validators=[RegexValidator(regex='^\+?[1-9]\d{1,14}$')],
                                    null=True, blank=True, max_length=15)
    business_phone_number = models.CharField(validators=[RegexValidator(regex='^\+?[1-9]\d{1,14}$')],
                                             null=True, blank=True, max_length=15)

    def user_directory_path(self, store_front):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        #print("Saved user " + self.account_holder + " AND " + self.acount_holder_id)
        print("Storing at user_{0}/storefront/{1}".format(self.user_id, self.store_front.__str__()))
        return 'user_{0}/storefront/{1}'.format(self.user_id, self.store_front.__str__())

    store_front = models.ImageField(upload_to=user_directory_path, default='/user/storefront/default-storefront.jpg')

    def __str__(self):
        return self.user.first_name + self.user.last_name

    def change_service_value(self, service_name, service_price):
        j = json.dumps(self.services, indent=4, sort_keys=True)
        loaded_j = json.loads(j)
        loaded_j[service_name] = service_price
        self.services = loaded_j

    class Meta:
        verbose_name = 'Stylista'
        verbose_name_plural = 'Stylistas'