from django.contrib import admin
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableAdminMixin

from .models import (
    SubCategory,
    Brand,
    Model,
    BodyType,
    Engine,
    Fuel,
    Transmission,
    DriveType,
    State,
    Color,
    AutoAdvert
)

@admin.register(SubCategory)
class AdminSubCategory(SortableAdminMixin, admin.ModelAdmin):
    """ Подкатегории объявлений """
    list_display = ('id', 'category', 'name',  'my_order', 'slug')
    list_display_links = ('category', 'name')
    
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
    list_display_links = ('name',)

@admin.register(Model)
class AdminModel(admin.ModelAdmin):
    """ Модели авто """
    list_display = ('id', 'sub_category', 'brand',  'name', 'slug')
    list_display_links = ('name', 'sub_category', 'brand',)

@admin.register(BodyType)
class AdminBodyType(admin.ModelAdmin):
    """ Тип кузова """
    list_display = ('id', 'name', 'slug')
    list_display_links = ('name',)

@admin.register(Engine)
class AdminEngine(admin.ModelAdmin):
    """ Двигатель """
    list_display = ('id', 'name', 'slug')
    list_display_links = ('name',)

@admin.register(Fuel)
class AdminFuel(admin.ModelAdmin):
    """ Топливо """
    list_display = ('id', 'name', 'slug')
    list_display_links = ('name',)

@admin.register(Transmission)
class AdminTransmission(admin.ModelAdmin):
    """ КПП """
    list_display = ('id', 'name', 'slug')
    list_display_links = ('name',)

@admin.register(DriveType)
class AdminTransmission(admin.ModelAdmin):
    """ Привод """
    list_display = ('id', 'name', 'slug')
    list_display_links = ('name',)

@admin.register(State)
class AdminState(admin.ModelAdmin):
    """ Состояние """
    list_display = ('id', 'name', 'slug')
    list_display_links = ('name',)

@admin.register(Color)
class AdminColor(admin.ModelAdmin):
    """ Цвет авто """
    def avatar_image(self, obj):
        if obj.avatar:
            return mark_safe(
                '<img src="{url}" width="25" height="25" />'.format(
                    url = obj.avatar.url
                )
            )
    avatar_image.allow_tags = True
    avatar_image.short_description = 'Аватар цвет'
    list_display = ('id', 'name', 'avatar_image', 'avatar', 'slug')
    readonly_fields = ['avatar_image',]
    list_display_links = ('name',)

@admin.register(AutoAdvert)
class AdminState(admin.ModelAdmin):
    """ Объявление о продаже авто """
    list_display = (
        'id',
        'brand',
        'model',
        'body_type',
        'engine',
        'fuel',
        'transmission',
        'drive_type',
        'production_year',
        'state',
        'color',
        'slug',
        'number_door',
        'number_seat',
        'wheel',
        'mileage'

    )
    list_display_links = (
        'brand',
        'model',
        'body_type',
        'engine',
        'fuel',
        'transmission',
        'drive_type',
        'state',
        'color'
    )
