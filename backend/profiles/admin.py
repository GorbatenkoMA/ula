from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Profile

@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    """ Профиль пользователя """
    def avatar_image(self, obj):
        print('==========================')
        if obj.avatar:
            return mark_safe(
                '<img src="{url}" width="50" height="25" />'.format(
                url = obj.avatar.url
                )
            )

    avatar_image.allow_tags = True
    avatar_image.short_description = 'Аватар фото'
    list_display = ('id', 'user', 'first_name', 'last_name', 'avatar_image', 'avatar', 'slug')
    readonly_fields = ['avatar_image',]
    list_display_links = ('user',)
