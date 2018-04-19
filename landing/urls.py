from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # /landing/1
    path('<int:stylist_id>/', views.detail, name='detail'),
    # /landing/name
    path('name/', views.name, name='name'),
]
