from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib import messages

from follow.models import Relation


# Create your views here.
class UserFollowView(LoginRequiredMixin, View):
    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        relation = Relation.objects.filter(from_user=request.user, to_user=user)
        if relation.exists():
            messages.error(request, ' You Follow Before', 'danger')
        else:
            Relation.objects.create(from_user=request.user, to_user=user)
            messages.success(request, ' You Follow ', 'success')
        return redirect('account:user_profile', user_id)


class UserUnFollowView(LoginRequiredMixin, View):
    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        relation = Relation.objects.filter(from_user=request.user, to_user=user)
        if relation.exists():
            relation.delete()
            messages.success(request, 'You unfollowed User', 'success')
        else:
            messages.erro(request, 'You can not unfollow User', 'error')
        return redirect('account:user_profile', user_id=user_id)
