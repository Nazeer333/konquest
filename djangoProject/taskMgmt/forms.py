#forms.py
from django import forms #repeat
from django.contrib.auth.forms import UserCreationForm #repeat
from django.contrib.auth.models import User #repeat
from .models import Profile, Task, Team, Location, Hunt, Clue
from django.db import transaction #repeat, where is this used?
import logging #repeat

logger = logging.getLogger(__name__)
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            # Profile creation is handled by signals
        return user

#admin
class AdminUserCreationForm(UserCreationForm):
    is_staff = forms.BooleanField(required=False)
    is_superuser = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'is_staff', 'is_superuser', 'password1', 'password2']

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'points', 'members']
        widgets = {
            'members': forms.CheckboxSelectMultiple,
        }

#Tasks
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'hunt', 'location', 'description', 'point_value']


#Clue
class ClueForm(forms.ModelForm):
    class Meta:
        model = Clue
        fields = ['name', 'description', 'location', 'task']


#location
class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name', 'description', 'latitude', 'longitude']

#hunt

class HuntForm(forms.ModelForm):
    class Meta:
        model = Hunt
        fields = ['name', 'description', 'start_time', 'end_time', 'event_date', 'location']

class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'John'}),
    )
    last_name = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Doe'}),
    )
    phone_number = forms.CharField(
        max_length=15,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': '+1234567890'}),
    )
    bio = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'placeholder': 'Write a brief description about yourself.'}),
    )
    location = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'City, Country'}),
    )
    birth_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD', 'type': 'date'}),
    )

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'phone_number', 'bio', 'location', 'birth_date']