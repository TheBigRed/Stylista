from django.contrib import admin
from .models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ('pk', 'account_holder_id', 'account_holder', 'stylist_type')


admin.site.register(Account, AccountAdmin)
