from django.urls import path
from . import views


app_name = 'core'
urlpatterns = [
    path('main/', views.main, name='main'),
    path('searchresults/', views.searchresults, name='searchresults'),
    path('searchrefined/', views.searchrefined, name='searchrefined'),
    path('searchrevolver/', views.stylistsearchmodule, name='searchrevolver'),
    #path('profile/', views.profile, name='profile'),
    path('profile/<store_front>/', views.profile, name='profile'),
    path('testbench', views.test_bench, name='test_bench'),
]
