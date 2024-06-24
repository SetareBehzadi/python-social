from django import forms

from post.models import Post, Comment


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('body', 'title')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }


class CommentReplyForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'col':5, 'row': 3})
        }
