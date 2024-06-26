from django.urls import path

from post.views import PostDetailView, PostDeleteView, PostEditView, PostCreatView, PostAddReplyView, PostLikeView

app_name = 'post'
urlpatterns = [
    path('details/<int:post_id>/<slug:post_slug>', PostDetailView.as_view(), name='post_detail'),
    path('delete/<int:post_id>', PostDeleteView.as_view(), name='post_delete'),
    path('edit/<int:post_id>', PostEditView.as_view(), name='post_edit'),
    path('create', PostCreatView.as_view(), name='post_create'),
    path('reply/<int:post_id>/<int:comment_id>', PostAddReplyView.as_view(), name='reply_comment'),
    path('like/<int:post_id>/', PostLikeView.as_view(), name='post_like'),
]