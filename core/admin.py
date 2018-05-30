from django.contrib import admin
from .models import Account, Gallery


class AccountAdmin(admin.ModelAdmin):
    list_display = ('pk', 'account_holder_id', 'account_holder', 'store_name', 'stylist_type')


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user_id', 'picture', 'caption', 'upload_time')


admin.site.register(Account, AccountAdmin)
admin.site.register(Gallery, GalleryAdmin)
