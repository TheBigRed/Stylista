from django.urls import path

from . import views


app_name = 'landing'
urlpatterns = [
    path('', views.index, name='index'),
    # /landing/1 ''' displays name of stylist when putting in primary key '''
    path('<int:stylist_id>/', views.stylist, name='stylist'),
    # /landing/name ''' Displays name of all clients in database '''
    path('name/', views.name, name='name'),
]
