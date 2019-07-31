from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('posts/<int:pk>', views.post_detail, name='post_detail'),
    path('posts/new', views.post_new, name='post_new'),
    path('posts/<int:pk>/edit', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('posts/<int:pk>/publish', views.post_publish, name='post_publish'),
    path('posts/<int:pk>/remove', views.post_remove, name='post_remove'),
]
