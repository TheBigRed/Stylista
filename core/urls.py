from django.urls import path
from . import views


app_name = 'core'
urlpatterns = [
    path('main/', views.main, name='main'),
    path('searchresults/', views.searchresults, name='searchresults'),
    path('searchrefined/', views.searchrefined, name='searchrefined'),
    path('upload/', views.uploadmodule, name='uploadmodule'),
]
