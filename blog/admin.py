from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin


from .models import Post, Comment, Category


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'slug', 'created_at', 'category']
    search_fields = ['title']
    list_filter = ('created_at', 'category')


class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'user', 'created_at']
    search_fields = ('user', 'body')
    list_filter = ('created_at',)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'slug']
    search_fields = ['title']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)