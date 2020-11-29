from .models import BlogPost
from django.contrib import admin


class BlogPostAdmin(admin.ModelAdmin):
    model = BlogPost
    readonly_fields = ('slug',)
    search_fields = ['title', 'body']


admin.site.register(BlogPost, BlogPostAdmin)
