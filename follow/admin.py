from django.contrib import admin
from django.contrib.admin import register
from follow.models import Relation


# admin.site.register(Relation)

@register(Relation)
class RelationModelAdmin(admin.ModelAdmin):
    list_display = ('from_user' , 'to_user', 'created_at')