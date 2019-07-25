from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

import datetime

from backend.ula.models import Category
from backend.utils import (
    gen_slug,
    get_path_brand_avatar,
    get_path_color_avatar,
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

class AutoAdvert(models.Model):
    """ Объявление о продаже авто """
    brand = models.ForeignKey(Brand, verbose_name='Марка', on_delete=models.CASCADE)
    model = models.ForeignKey(Model, verbose_name='Модель', on_delete=models.CASCADE)
    body_type = models.ForeignKey(BodyType, verbose_name='Тип кузова', on_delete=models.CASCADE)
    engine = models.ForeignKey(Engine, verbose_name='Двигатель', on_delete=models.CASCADE)
    fuel = models.ForeignKey(Fuel, verbose_name='Топливо', on_delete=models.CASCADE)
    transmission = models.ForeignKey(Transmission, verbose_name='КПП', on_delete=models.CASCADE)
    drive_type = models.ForeignKey(DriveType, verbose_name='Привод', on_delete=models.CASCADE)
    state = models.ForeignKey(State, verbose_name='Состояние', on_delete=models.CASCADE)
    color = models.ForeignKey(Color, verbose_name='Цвет', on_delete=models.CASCADE)
    slug = models.SlugField('Слаг', max_length=100, unique=True, blank=True, editable=False)
    production_year = models.PositiveIntegerField(
        verbose_name='Год выпуска',
        default=datetime.date.today().year,
        validators=(MinValueValidator(1991), MaxValueValidator(datetime.date.today().year))
    )
    number_door = models.IntegerField('Количество дверей', default=4, choices=[(i,i) for i in range(2, 6)])
    number_seat = models.IntegerField('Количество мест', default=2, choices=[(i,i) for i in range(2, 8)])
    wheel = models.CharField('Руль', max_length=10, default=1, choices=[('L', 'Левый'), ('R', 'Правый')])
    mileage = models.PositiveIntegerField('Пробег', default=0)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.id

    def save(self, **kwargs):
        self.slug = gen_slug(self.id)
        super().save(**kwargs)
