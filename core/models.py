from django.db import models
from landing.models import Stylist
from core.forms import UploadFileForm

class Account(models.Model):
    account_holder = models.ForeignKey(Stylist, models.CASCADE, related_name='account')
    stylist_type = models.CharField(max_length=25, blank=True)
    location = models.CharField(max_length=25, blank=True)
    store_front = models.ImageField(upload_to='user/storefront/', default='/user/storefront/upload.jpg')

    def __str__(self):
        return self.account_holder

    def user_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return 'user_{0}/{1}'.format(instance.account_holder, UploadFileForm.cleaned_data['file'])
