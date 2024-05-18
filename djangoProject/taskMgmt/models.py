#models.py

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    points = models.IntegerField(default=0)
    members = models.ManyToManyField('auth.User', related_name='teams')

class Location(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return self.name

class Hunt(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    event_date = models.DateField(null=True, blank=True)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    point_value = models.IntegerField(default=1)
    hunt = models.ForeignKey('Hunt', on_delete=models.CASCADE)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Clue(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    task = models.ForeignKey('Task', on_delete=models.CASCADE, related_name='clues')

    def __str__(self):
        return self.name





def __str__(self):
        return self.title
