# create_profiles.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from taskMgmt.models import Profile

class Command(BaseCommand):
    help = 'Create profiles only for active users who don’t already have them'

    def handle(self, *args, **kwargs):
        created_profiles = 0
        for user in User.objects.filter(is_active=True):
            if not hasattr(user, 'profile'):
                Profile.objects.create(user=user, bio="New user profile")  # Example field
                created_profiles += 1
                self.stdout.write(self.style.SUCCESS(f'Created profile for {user.username}'))

        self.stdout.write(self.style.SUCCESS(f'Total Profiles Created: {created_profiles}'))