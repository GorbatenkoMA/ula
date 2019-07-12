from django.contrib import admin
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableAdminMixin

from .models import SubCategory, Brand

@admin.register(SubCategory)
class AdminSubCategory(SortableAdminMixin, admin.ModelAdmin):
    """ Подкатегории объявлений """
    list_display = ('id', 'category', 'name',  'my_order', 'slug')

@admin.register(Brand)
class AdminBrandy(admin.ModelAdmin):
    """ Марка авто """
    def avatar_image(self, obj):
        if obj.avatar:
            return mark_safe(
                '<img src="{url}" width="50" height="25" />'.format(
                    url = obj.avatar.url
                )
            )
    avatar_image.allow_tags = True
    avatar_image.short_description = 'Аватар фото'
    list_display = ('id', 'name', 'avatar_image', 'avatar', 'slug')
    readonly_fields = ['avatar_image',]
