from django.urls import path
from . import views


app_name = 'booking'
urlpatterns = [
    path('contract/', views.main, name='main'),
]
