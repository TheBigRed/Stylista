from django.contrib import admin
from .models import Stylist, Client, Stylista


class StylistAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'last_name', 'email', 'password', 'joined_date')


class ClientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'zip_code', 'address')


class StylistaAdmin(admin.ModelAdmin):
    list_display = ('pk', 'business_name', 'business_id', 'business_phone_number', 'services', 'store_front')


admin.site.register(Stylist, StylistAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Stylista, StylistaAdmin)
