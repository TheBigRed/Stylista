from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Stylist, Client, Stylista
from django.contrib.auth.models import User


class StylistAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'last_name', 'email', 'password', 'joined_date')


class ClientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username', 'user_firstname', 'user_lastname','zip_code', 'address')

    def username(self, x):
        return x.user.username

    def user_firstname(self, x):
        return x.user.first_name

    def user_lastname(self, x):
        return x.user.last_name


class ClientAdminInline(admin.StackedInline):
    model = Client
    can_delete = False
    verbose_name_plural = 'clients'
    list_display = ('pk', 'zip_code', 'address')


class StylistaAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username', 'business_name', 'business_id', 'services', 'store_front')

    def username(self, x):
        return x.user.username

    def user_firstname(self, x):
        return x.user.first_name

    def user_lastname(self, x):
        return x.user.last_name


class UserAdmin(BaseUserAdmin):
    inlines = (ClientAdminInline,)

admin.site.unregister(User)
admin.site.register(Stylist, StylistAdmin)
admin.site.register(Stylista, StylistaAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Client, ClientAdmin)