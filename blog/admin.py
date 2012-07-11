from django.contrib import admin
from models import Post


class PostAdmin(admin.ModelAdmin):
    model = Post
    search_fields = ["title", "content"]
    list_filter = ["status", "published", ]
    list_display = ["title", "content", "status", "published"]
    prepopulated_fields = {'slug': ('title',), }

admin.site.register(Post, PostAdmin)
