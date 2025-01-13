from django.contrib import admin
from .models import Post, Category
from django_mptt_admin.admin import DjangoMpttAdmin

@admin.register(Category)
class CategoryAdmin(DjangoMpttAdmin):
    """
    Админ-панели модели другой категории
    """
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post)
