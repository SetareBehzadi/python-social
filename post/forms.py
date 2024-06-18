from django import forms

from post.models import Post


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('body', 'title')