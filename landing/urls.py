from django.urls import path, re_path
from . import views


app_name = 'landing'
urlpatterns = [
    path('', views.index, name='index'),
    # /landing/1 ''' displays name of stylist when putting in primary key '''
    path('<int:stylist_id>/', views.stylist, name='stylist'),
    # /landing/name ''' Displays name of all clients in database '''
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('newuser/', views.newuser, name='newuser'),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('authentication/', views.authentication, name='authentication'),
    path('account/<kottai>', views.account, name='account'),
    path('about/', views.about, name='about'),
]
