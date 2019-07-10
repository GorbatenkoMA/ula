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

def get_path_upload_avatar(instance, filename):
    """
    return: profile/username/username_avatar.jpg
    """
    path = Path(filename)
    imagepath = 'profile/{username}/{username}_avatar{suffix}'.format(
        username=instance.user.username,
        suffix=path.suffix
    ).lower()
    fullname = os.path.join(settings.MEDIA_ROOT, imagepath)
    if os.path.exists(fullname):
        os.remove(fullname)
    return imagepath
