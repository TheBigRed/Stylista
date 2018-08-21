from django.db import models
from landing.models import Stylist
from core.forms import UploadFileForm


class Account(models.Model):

    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    STYLISTA_TYPES = (
        ('BARBER', 'Barber'),
        ('HAIR_STYLIST', 'Hair Stylist'),
        ('MAKEUP', 'Makeup Artist'),
        ('MUAH', 'Make Up And Hair'),
        ('NAILS', 'Nail Technician'),
        ('CLIENT', 'Client'),
    )

    account_holder = models.ForeignKey(Stylist, models.CASCADE, related_name='account')
    store_name = models.CharField(max_length=25, blank=True)
    stylist_type = models.CharField(max_length=25, choices=STYLISTA_TYPES, blank=True)
    gender = models.CharField(max_length=25, choices=GENDER, blank=True)
    address = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=25, blank=True)
    location = models.CharField(max_length=25, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    about_me = models.TextField(blank=True)

    def user_directory_path(self, store_front):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        #print("Saved user " + self.account_holder + " AND " + self.acount_holder_id)
        return 'user_{0}/storefront/{1}'.format(self.account_holder_id, self.store_front.__str__())

    store_front = models.ImageField(upload_to=user_directory_path, default='/user/storefront/default-storefront.jpg')
    #store_front = models.ImageField(upload_to='kottai/test', default='/user/storefront/upload.jpg')

    #def __str__(self):
        #return self.account_holder

    # def get_gallery(self):
    #     return self.gallery_set.all()


class Gallery(models.Model):
    user = models.ForeignKey(Stylist, models.CASCADE)
    caption = models.CharField(max_length=50, blank=True)
    upload_time = models.DateTimeField(auto_now_add=True)

    def user_directory_path1(self, picture):
        return 'user_{0}/gallery/{1}'.format(self.user_id, self.picture.__str__())

    picture = models.ImageField(upload_to=user_directory_path1, default='/user/gallery/gallery.jpg')


class Service(models.Model):
    user = models.ForeignKey(Stylist, models.CASCADE)
    service_name = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=50, blank=True)
    duration = models.DurationField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
