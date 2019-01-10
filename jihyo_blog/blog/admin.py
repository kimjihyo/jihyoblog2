from django.contrib import admin
from .models import Tag, Comment, Post

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 1

class PostAdmin(admin.ModelAdmin):
    inline = [CommentInline]

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
