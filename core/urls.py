from django.urls import path
from . import views


app_name = 'core'
urlpatterns = [
    path('main/<stylist>', views.main, name='main'),
    path('searchresults/', views.searchresults, name='searchresults'),
]
