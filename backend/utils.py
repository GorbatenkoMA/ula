from django.utils.text import slugify

from time import time
from pathlib import Path

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
    return '{stem}-{time}{suffix}'.format(
        stem=path.stem[:50],
        time=str(int(time())),
        suffix=path.suffix
    ).lower()

def get_path_category_avatar(instance, filename):
    """ путь для загрузки аватарки модели ula.models.Category """
    path = Path(filename)
    return 'category_avatar/{}'.format(gen_image_name(filename))
