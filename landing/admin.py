from django.contrib import admin
from .models import Stylist


class StylistaAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'joined_date')


admin.site.register(Stylist, StylistaAdmin)