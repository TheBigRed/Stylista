from django.db import models
from landing.models import Stylist
from core.forms import UploadFileForm


class Account(models.Model):
    account_holder = models.ForeignKey(Stylist, models.CASCADE, related_name='account')
    stylist_type = models.CharField(max_length=25, blank=True)
    location = models.CharField(max_length=25, blank=True)

    def user_directory_path(self, store_front):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return 'user_{0}/storefront/{1}'.format(self.account_holder_id, self.store_front.__str__())

    store_front = models.ImageField(upload_to=user_directory_path, default='/user/storefront/upload.jpg')
    #store_front = models.ImageField(upload_to='kottai/test', default='/user/storefront/upload.jpg')

    def __str__(self):
        return self.account_holder
