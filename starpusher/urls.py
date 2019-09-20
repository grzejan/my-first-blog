from django.urls import path
from . import views

urlpatterns = [
    path('starpusher/', views.starpusher, name='starpusher'),
]