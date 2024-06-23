from django.contrib import admin
from django.contrib.admin import register
from post.models import Post, Comment


@register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'body', 'slug')
    search_fields = ('title','slug')
    list_filter = ('created_at',)
    prepopulated_fields = {"slug":('title',)}
    raw_id_fields = ('user',)


@register(Comment)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'created_at', 'is_reply']
    raw_id_fields = ['user', 'post', 'reply']
