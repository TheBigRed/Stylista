from django.urls import path
from . import views


app_name = 'reviews'
urlpatterns = [
    path('', views.reviews, name='reviews'),
    path('comment/', views.comment, name='comment'),
    path('upvote/', views.upvote, name='upvote'),
]
