from django.urls import path, re_path
import core.views

from . import views


app_name = 'landing'
urlpatterns = [
    path('', views.index, name='index'),
    # /landing/1 ''' displays name of stylist when putting in primary key '''
    path('<int:stylist_id>/', views.stylist, name='stylist'),
    # /landing/name ''' Displays name of all clients in database '''
    path('name/', views.name, name='name'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('newuser/', views.newuser, name='newuser'),
    path('thankyou/<fullname>/', views.thankyou, name='thankyou'),
    path('authenticate/', views.authenticate, name='authenticate'),
    path('account/<kottai>', views.account, name='account'),
    path('about/', views.about, name='about'),
    #path('core/account', core.views.index, name='account'),
]
