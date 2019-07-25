from django.utils.text import slugify, get_valid_filename
from django.conf import settings


from time import time
from pathlib import Path
import os

from backend import ula, transport, profiles

alphabet = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
            'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
            'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'i', 'э': 'e', 'ю': 'yu',
            'я': 'ya', 'ь':'', 'ъ':''}

def gen_slug(value):
    new_slug = ''.join(alphabet.get(s, s) for s in slugify(value, allow_unicode=True))[:50]
    return new_slug + '-' + str(int(time()))

def gen_image_name(filename):
    """ image_name.jpg -> image_name-1562836816.jpg """
    path = Path(filename)
    return get_valid_filename('{stem}-{time}{suffix}'.format(
        stem=path.stem[:50],
        time=str(int(time())),
        suffix=path.suffix
    ).lower())

def get_path_category_avatar(instance, filename):
    """ путь для загрузки аватарки модели ula.models.Category """
    path = Path(filename)
    return 'category_avatar/{}'.format(gen_image_name(filename))

def get_path_brand_avatar(instance, filename):
    """ путь для загрузки аватарки модели transport.models.Brand """
    path = Path(filename)
    return 'brand_avatar/{}'.format(gen_image_name(filename))

def get_path_color_avatar(instance, filename):
    """ путь для загрузки аватарки модели transport.models.Color """
    path = Path(filename)
    return 'color_avatar/{}'.format(gen_image_name(filename))

def get_path_profile_avatar(instance, filename):
    """ путь для загрузки аватарки модели profiles.models.Profile """
    path = Path(filename)
    return 'users_avatar/{username}/{avatar_name}/'.format(
        username=instance.user.username,
        avatar_name=gen_image_name(filename)
    )

def clean_image(files, path):
     files_del = set(os.listdir(path)) - set([Path(file).name for file in files if file])
     for file in files_del:
         os.remove('{}\{}'.format(path, file))

def clean_image_test(files, path):
     files_del = set(os.listdir(path)) - set([Path(file).name for file in files if file])
     print(files_del)
     for file in files_del:
         os.remove('{}\{}'.format(path, file))

def clean_image_category_avatar():
    path = '{}\{}'.format(settings.MEDIA_ROOT, 'category_avatar')
    files = [obj['avatar'] for obj in ula.models.Category.objects.all().values('avatar')]
    clean_image(files, path)

def clean_image_brand_avatar():
    path = '{}\{}'.format(settings.MEDIA_ROOT, 'brand_avatar')
    files = [obj['avatar'] for obj in ula.models.Brand.objects.all().values('avatar')]
    clean_image(files, path)

def clean_image_profile_avatar():
    for obj in profiles.models.Profile.objects.all():
        path = '{}\{}\{}'.format(settings.MEDIA_ROOT, 'users_avatar', obj.user.username)
        if obj.avatar:
            files = [obj.avatar.url]
            clean_image(files, path)
