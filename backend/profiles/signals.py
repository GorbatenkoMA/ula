from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from backend import profiles

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profiles.models.Profile.objects.create(user=instance)
