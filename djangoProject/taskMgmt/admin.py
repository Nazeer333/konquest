#admin.py
from django.contrib import admin
from .models import Location, Hunt, Task, Clue, Profile


class LocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'latitude', 'longitude']

class HuntAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'start_time', 'end_time', 'event_date', 'location']

class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'point_value', 'hunt', 'location']

class ClueAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'task', 'location']

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name']

admin.site.register(Location)
admin.site.register(Hunt)
admin.site.register(Task)
admin.site.register(Clue)
admin.site.register(Profile)