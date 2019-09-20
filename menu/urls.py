from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('echo/', views.echo, name='echo'),
]