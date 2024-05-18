# taskMgmt/management/commands/create_missing_profiles.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from taskMgmt.models import Profile

class Command(BaseCommand):
    help = 'Create missing profiles for existing users'

    def handle(self, *args, **kwargs):
        users_without_profiles = User.objects.filter(profile__isnull=True)
        for user in users_without_profiles:
            Profile.objects.create(user=user)
            self.stdout.write(self.style.SUCCESS(f'Created profile for user {user.username}'))