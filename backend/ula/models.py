from django.db import models
from backend.utils import gen_slug, get_path_upload_avatar

class Category(models.Model):
    """ Категории объявлений """
    slug = models.SlugField('slug', max_length=100, unique=True, blank=True, editable=False)
    name = models.CharField('Имя', max_length=100, unique=True)
    avatar = models.ImageField("Аватар", upload_to=get_path_upload_avatar, blank=True, null=True)


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        self.slug = gen_slug(self.name)
        super().save(**kwargs)
