from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('landing/', include('landing.urls')),
    path('core/', include('core.urls')),
    path('admin/', admin.site.urls),
]
