from django.contrib import admin
from .models import Stylist, Client


class StylistaAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'last_name', 'email', 'password', 'joined_date')


class ClientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'zip_code', 'address')


admin.site.register(Stylist, StylistaAdmin)
admin.site.register(Client, ClientAdmin)
