from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.post_list, name='post_list'),
    path('blog/posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('blog/posts/new/', views.post_new, name='post_new'),
    path('blog/posts/<int:post_id>/edit/', views.post_edit, name='post_edit'),
    path('blog/drafts/', views.post_draft_list, name='post_draft_list'),
    path('blog/posts/<int:post_id>/publish/', views.post_publish, name='post_publish'),
    path('blog/posts/<int:post_id>/remove/', views.post_remove, name='post_remove'),
    path('blog/posts/<int:post_id>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
]
