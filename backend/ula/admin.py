from django.contrib import admin

from .models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """ Категории объявлений """
    list_display = ('id', 'name', 'slug')
    ordering = ('id', )