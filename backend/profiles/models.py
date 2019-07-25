from django.db import models
from django.contrib.auth.models import User

from backend.utils import get_path_profile_avatar, gen_slug

from .signals import create_user_profile

class Profile(models.Model):
    """ Профиль пользователя """
    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    slug = models.SlugField('Слаг', max_length=100, unique=True, blank=True, editable=False)
    avatar = models.ImageField("Аватар путь", upload_to=get_path_profile_avatar, blank=True)
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профиля'

    def __str__(self):
        return self.user.username

    def save(self, **kwargs):
        self.slug = gen_slug(self.user.username)
        super().save(**kwargs)
