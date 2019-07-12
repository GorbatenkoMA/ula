from django.db import models

from pathlib import Path

from backend.utils import gen_slug, get_path_category_avatar


class Category(models.Model):
    """ Категории объявлений """
    slug = models.SlugField('Слаг', max_length=100, unique=True, blank=True, editable=False)
    my_order = models.PositiveIntegerField('Порядок', default=0, blank=False, null=False)
    name = models.CharField('Категория', max_length=100, unique=True)
    avatar = models.ImageField("Аватар путь", upload_to=get_path_category_avatar, blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['my_order',]

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        self.slug = gen_slug(self.name)
        super().save(**kwargs)
