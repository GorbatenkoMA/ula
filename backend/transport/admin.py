from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin

from .models import SubCategory

@admin.register(SubCategory)
class AdminSubCategory(SortableAdminMixin, admin.ModelAdmin):
    """ Подкатегории объявлений """
    list_display = ('id', 'category', 'name',  'my_order', 'slug')
