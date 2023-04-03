from django.contrib import admin
from .models import Category, Post


class CategoryInline(admin.TabularInline):
    """Assign posts with category's"""
    model = Post.category.through


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """ Admin panel for category's """
    inlines = [
        CategoryInline,
    ]
    list_display = ('category_name',)
    fields = ('category_name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """ Admin panel for post's """
    list_display = ('title', 'date', 'main_category')
    fields = ('title', 'text', 'date', 'main_category', 'category')
