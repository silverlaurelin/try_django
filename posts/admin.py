from django.contrib import admin

# Register your models here.

from .models import Post
class PostAdminModel (admin.ModelAdmin):
    list_display = ["title", "updated" ,"timestamp"]
    list_editable = ["title"]
    list_display_links = ["updated"]
    list_filter = ["timestamp"]
    search_fields = ["title", "content"]
    class Meta:
        model=Post


admin.site.register(Post, PostAdminModel)
