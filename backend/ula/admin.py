from django.contrib import admin
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableAdminMixin

from .models import Category

@admin.register(Category)
class CategoryAdmin(SortableAdminMixin, admin.ModelAdmin):
    """ Категории объявлений """
    def avatar_image(self, obj):
        if obj.avatar:
            return mark_safe(
                '<img src="{url}" width="100" height="50" />'.format(
                    url = obj.avatar.url
                )
            )
    avatar_image.allow_tags = True
    avatar_image.short_description = 'Аватар фото'
    list_display = ('id', 'name', 'avatar_image', 'avatar', 'my_order', 'slug')
    readonly_fields = ['avatar_image',]
