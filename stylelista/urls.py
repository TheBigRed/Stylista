from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('landing/', include('landing.urls')),
    path('core/', include('core.urls')),
    path('usersettings/', include('usersettings.urls')),
    path('booking/', include('booking.urls')),
    path('reviews/', include('reviews.urls')),
    path('messages/', include('messages.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
