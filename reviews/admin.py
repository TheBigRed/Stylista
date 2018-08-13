from django.contrib import admin
from .models import Review


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'client_id', 'stylist_id', 'title', 'review', 'rating')


admin.site.register(Review, ReviewsAdmin)