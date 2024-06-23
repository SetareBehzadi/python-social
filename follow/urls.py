from django.urls import path

from follow.views import UserFollowView, UserUnFollowView

app_name = 'follow'

urlpatterns = [
    path('<int:user_id>/', UserFollowView.as_view(), name= 'user_follow'),
    path('unfollow/<int:user_id>/', UserUnFollowView.as_view(), name= 'user_unfollow'),
]