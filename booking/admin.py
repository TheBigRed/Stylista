from django.contrib import admin
from .models import Contract


class ContractAdmin(admin.ModelAdmin):
    list_display = ('pk', 'client_id', 'stylist_id', 'date', 'time', 'total_price')


admin.site.register(Contract, ContractAdmin)