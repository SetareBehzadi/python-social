from django.contrib import admin
from django.contrib.admin import register
from post.models import Post


@register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'body', 'slug')
    search_fields = ('title','slug')
    list_filter = ('created_at',)
    prepopulated_fields = {"slug":('title',)}
    raw_id_fields = ('user',)
