# signals.py
from django.db.models.signals import post_save #repeat
from django.contrib.auth.models import User #repeat
from django.dispatch import receiver #repeat
from .models import Profile #repeat
import logging #repeat

logger = logging.getLogger(__name__)

# Signal to create or update profile when user is created
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        logger.debug(f'Profile created for user: {instance.username}')
    else:
        instance.profile.save()
        logger.debug(f'Profile updated for user: {instance.username}')

'''@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)'''

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# Connect the signal to the User model's post_save event
post_save.connect(create_or_update_user_profile, sender=User)