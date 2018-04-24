from django.urls import path

from . import views


app_name = 'landing'
urlpatterns = [
    path('', views.index, name='index'),
    # /landing/1 ''' displays name of stylist when putting in primary key '''
    path('<int:stylist_id>/', views.stylist, name='stylist'),
    # /landing/name ''' Displays name of all clients in database '''
    path('name/', views.name, name='name'),
    path('signup/', views.signup, name='signup'),
    path('newuser/', views.newuser, name='newuser'),
    path('thankyou/(?P<fullname>[\w\-]+)/$', views.thankyou, name='thankyou'),
    path('about/', views.about, name='about'),
]
