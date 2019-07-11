from django.db import models

from backend.ula.models import Category
from backend.utils import gen_slug


class SubCategory(models.Model):
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    my_order = models.PositiveIntegerField('Порядок', default=0, blank=False, null=False)
    slug = models.SlugField('slug', max_length=100, unique=True, blank=True, editable=False)
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
