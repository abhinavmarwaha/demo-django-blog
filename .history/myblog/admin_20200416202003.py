from django.contrib import admin
from django_summernote.admin import SummernoteInlineModelAdmin
from .models import Post, Comment

class PostAdmin(SummernoteInlineModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    summernote_fields = ('conten')
    list_filter = ["status"]
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

class AdminComment(admin.ModelAdmin):
    list_display = ('name','body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active = True)
    
admin.site.register(Comment, AdminComment)
admin.site.register(Post, PostAdmin)