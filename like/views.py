from django.shortcuts import render
from django.views import View

from like.models import Like


# Create your views here.
class LikeView(View):
    def get(self, request, contentType):

        like = Like.objects.create(user=request.user, content_type=contentType)