from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin

from .models import Category

# TODO: отображение в админке aватарки
@admin.register(Category)
class CategoryAdmin(SortableAdminMixin, admin.ModelAdmin):
    """ Категории объявлений """
    list_display = ('id', 'name', 'avatar', 'my_order', 'slug')
