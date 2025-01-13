from django.contrib import admin
from .models import Post, Category
from mptt.admin import DraggableMPTTAdmin

@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    """
    Админ-панели модели другой категории
    """
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post)
