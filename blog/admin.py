from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

# Register your models here.

from .models import Post, Category, Tag

admin.site.register(Post, MarkdownxModelAdmin)

class CategoryAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('name', )}

class TagAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('name', )}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)