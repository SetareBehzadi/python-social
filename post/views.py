from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils.text import slugify
from post.forms import PostUpdateForm, CommentForm
from post.models import Post


class PostDetailView(View):
    form_class = CommentForm

    def setup(self, request, *args, **kwargs):
        self.post_instance = get_object_or_404(Post, pk=kwargs['post_id'], slug=kwargs['post_slug'])
        return super().setup(request, *args, **kwargs)

    def get(self, request,  *args, **kwargs):
        #post = Post.objects.get(pk=post_id, slug=post_slug)
        post = self.post_instance
        comments = post.pcomments.filter(is_reply=False)
        return render(request, 'show.html', {'post': post, 'comments': comments, 'form': self.form_class})

    # @login_required =>function decorator x
    @method_decorator(login_required)
    def post(self, request,  *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.post = self.post_instance
            new_comment.save()
            messages.success(request,'comment is submitted', 'success')
        return redirect('post:post_detail', self.post_instance.id , self.post_instance.slug)


class PostDeleteView(LoginRequiredMixin, View):
    def get(self, request, post_id):
        post = Post.objects.get(pk=post_id)
        if post.user.id == request.user.id:
            post.delete()
            messages.success(request, 'Post is Deleted successfully', 'success')
        else:
            messages.error(request, 'Post can not be deleted', 'error')
        return redirect('home:home')


class PostEditView(LoginRequiredMixin, View):
    form_class = PostUpdateForm

    def setup(self, request, *args, **kwargs):
        self.post_instance = Post.objects.get(pk=kwargs['post_id'])
        return super().setup(request,*args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        post = self.post_instance
        if not post.user.id == request.user.id:
            messages.error(request, 'Post can not be edited', 'error')
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)
    def get(self, request, post_id):
        post = self.post_instance
        form = self.form_class(instance=post)
        return render(request, 'update.html', {'form': form})

    def post(self, request, post_id):
        post = self.post_instance
        form = self.form_class(request.POST, instance=post)
        if form.is_valid():
            newPost = form.save(commit=False)
            newPost.slug = slugify(form.cleaned_data['title'][:30])
            newPost.save()

            messages.success(request, 'update successfully', 'success')
            return redirect('post:post_detail', post.id, post.slug)


class PostCreatView(LoginRequiredMixin, View):
    form_class = PostUpdateForm

    def get(self, request):
        form =self.form_class
        return render(request, 'update.html', {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.slug = slugify(form.cleaned_data['title'][:30])
            new_post.save()
            messages.success(request, 'create successfully', 'success')
            return redirect('post:post_detail', new_post.id, new_post.slug)
