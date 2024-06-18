from django.shortcuts import render
from django.views import View

from post.models import Post


class HomeView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'home/index.html',{'posts':posts})

    def post(self, request):
        return render(request, 'home/index.html')

from django.http import Http404
from django.shortcuts import render

def trigger_404(request):
    raise Http404("Page not found")