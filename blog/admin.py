from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('title', 'slug')
    search_fields = ('title')
    list_editable = ('title', 'slug')
    list_per_page = 10
    ordering = ('title')
    
