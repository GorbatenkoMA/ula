from django.db import models

from backend.ula.models import Category
from backend.utils import (
    gen_slug,
    get_path_brand_avatar,
    get_path_color_avatar
)


class SubCategory(models.Model):
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    my_order = models.PositiveIntegerField('Порядок', default=0, blank=False, null=False)
    slug = models.SlugField('Слаг', max_length=100, unique=True, blank=True, editable=False)
    name = models.CharField('Подкатегория', max_length=100, unique=True )

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'
        ordering = ['my_order',]

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        self.slug = gen_slug(self.name)
        super().save(**kwargs)

class Brand(models.Model):
    """ Марка авто """
    name = models.CharField('Марка', max_length=100, unique=True)
    slug = models.SlugField('Слаг', max_length=100, unique=True, blank=True, editable=False)
    avatar = models.ImageField("Аватар путь", upload_to=get_path_brand_avatar, blank=True)

    class Meta:
        verbose_name = 'Марка'
        verbose_name_plural = 'Марки'
        ordering = ['name',]

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        self.slug = gen_slug(self.name)
        super().save(**kwargs)

class Model(models.Model):
    """ Модель авто """
    sub_category = models.ForeignKey(SubCategory, verbose_name='Категория', on_delete=models.CASCADE, )
    brand = models.ForeignKey(Brand, verbose_name='Марка', on_delete=models.CASCADE)
    name = models.CharField('Модель', max_length=100, unique=True)
    slug = models.SlugField('Слаг', max_length=100, unique=True, blank=True, editable=False)

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'
        ordering = ['name',]

    def __str__(self):
        return self.name


        def save(self, **kwargs):
            self.slug = gen_slug(self.name)
            super().save(**kwargs)

class BodyType(models.Model):
    """ Тип кузова """
    name = models.CharField('Тип кузова', max_length=100, unique=True)
    slug = models.SlugField('Слаг', max_length=100, unique=True, blank=True, editable=False)

    class Meta:
        verbose_name = 'Тип кузова'
        verbose_name_plural = 'Тип кузова'
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        self.slug = gen_slug(self.name)
        super().save(**kwargs)

class Engine(models.Model):
    """ Двигатель """
    name = models.CharField('Двигатель', max_length=100, unique=True)
    slug = models.SlugField('Слаг', max_length=100, unique=True, blank=True, editable=False)

    class Meta:
        verbose_name = 'Двигатель'
        verbose_name_plural = 'Двигатели'
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        self.slug = gen_slug(self.name)
        super().save(**kwargs)

class Fuel(models.Model):
    """ Топливо """
    name = models.CharField('Топливо', max_length=100, unique=True)
    slug = models.SlugField('Слаг', max_length=100, unique=True, blank=True, editable=False)

    class Meta:
        verbose_name = 'Топливо'
        verbose_name_plural = 'Топливо'
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        self.slug = gen_slug(self.name)
        super().save(**kwargs)

class Transmission(models.Model):
    """ КПП """
    name = models.CharField('КПП', max_length=100, unique=True)
    slug = models.SlugField('Слаг', max_length=100, unique=True, blank=True, editable=False)

    class Meta:
        verbose_name = 'КПП'
        verbose_name_plural = 'КПП'
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        self.slug = gen_slug(self.name)
        super().save(**kwargs)

class DriveType(models.Model):
    """ Привод """
    name = models.CharField('Привод', max_length=100, unique=True)
    slug = models.SlugField('Слаг', max_length=100, unique=True, blank=True, editable=False)

    class Meta:
        verbose_name = 'Привод'
        verbose_name_plural = 'Привод'
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        self.slug = gen_slug(self.name)
        super().save(**kwargs)

class State(models.Model):
    """ Состояние """
    name = models.CharField('Состояние', max_length=100, unique=True)
    slug = models.SlugField('Слаг', max_length=100, unique=True, blank=True, editable=False)

    class Meta:
        verbose_name = 'Состояние'
        verbose_name_plural = 'Состояние'
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        self.slug = gen_slug(self.name)
        super().save(**kwargs)

class Color(models.Model):
    """ Цвет """
    name = models.CharField('Цвет', max_length=100, unique=True)
    slug = models.SlugField('Слаг', max_length=100, unique=True, blank=True, editable=False)
    avatar = models.ImageField("Ават цвета", upload_to=get_path_color_avatar, blank=True)

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвет'
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        self.slug = gen_slug(self.name)
        super().save(**kwargs)
