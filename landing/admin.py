from django.contrib import admin
from .models import Stylist


class StylistaAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'last_name', 'email', 'password', 'joined_date')


admin.site.register(Stylist, StylistaAdmin)