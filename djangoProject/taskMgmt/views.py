# views.py

# IMPORTS
# imports django
from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

# imports models
from .models import Task, Profile, Team, Location, Clue, Hunt

# imports forms
from .forms import ProfileForm, TaskForm, TeamForm, AdminUserCreationForm, RegisterForm, LocationForm, ClueForm, HuntForm

# database
from django.db import transaction

# import
import logging

logger = logging.getLogger(__name__)

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# admin
def is_admin(user):
    if not user.is_authenticated:
        return False
    if not user.is_superuser:
        messages.error(user, 'You must be an administrator to access that page.')
        return False
    return True

@user_passes_test(lambda u: u.is_superuser)
def create_user(request):
    if request.method == 'POST':
        form = AdminUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = AdminUserCreationForm()
    return render(request, 'admin/create_user.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def user_list(request):
    user_list = User.objects.all()
    paginator = Paginator(user_list, 50)  # Show 50 users per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'admin/user_list.html', {'page_obj': page_obj})

# teams
@login_required
def team_list(request):
    teams = Team.objects.all()
    return render(request, 'taskMgmt/team_list.html', {'teams': teams})

@login_required
@user_passes_test(is_admin)
def add_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Team added successfully.')
            return redirect('team_list')
    else:
        form = TeamForm()
    return render(request, 'taskMgmt/team_form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def edit_team(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    if request.method == 'POST':
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            form.save()
            return redirect('team_list')
    else:
        form = TeamForm(instance=team)
    return render(request, 'taskMgmt/team_form.html', {'form': form})

# profiles
@login_required
def profile(request):
    try:
        profile = request.user.profile
    except ObjectDoesNotExist:
        profile = None

    return render(request, 'taskMgmt/profile.html', {'user': request.user, 'profile': profile})

@login_required
def edit_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'taskMgmt/edit_profile.html', {'form': form})

# locations
@user_passes_test(lambda u: u.is_superuser)
def location_list(request):
    locations = Location.objects.all()
    return render(request, 'locations/location_list.html', {'locations': locations})

@user_passes_test(lambda u: u.is_superuser)
def add_location(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Location added successfully.')
            return redirect('location_list')
    else:
        form = LocationForm()
    return render(request, 'locations/location_form.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def edit_location(request, location_id):
    location = get_object_or_404(Location, pk=location_id)
    if request.method == 'POST':
        form = LocationForm(request.POST, instance=location)
        if form.is_valid():
            form.save()
            messages.success(request, 'Location updated successfully.')
            return redirect('location_list')
    else:
        form = LocationForm(instance=location)
    return render(request, 'locations/location_form.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def delete_location(request, location_id):
    location = get_object_or_404(Location, pk=location_id)
    if request.method == 'POST':
        location.delete()
        messages.success(request, 'Location deleted successfully.')
        return redirect('location_list')
    return render(request, 'locations/location_confirm_delete.html', {'location': location})

# tasks
@login_required
def task_list(request):
    tasks = Task.objects.all()
    is_admin = request.user.is_superuser
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'is_admin': is_admin})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task added successfully.')
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully.')
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted successfully.')
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

# clues
@login_required
@user_passes_test(lambda u: u.is_superuser)
def clue_list(request):
    clues = Clue.objects.all()
    return render(request, 'clues/clue_list.html', {'clues': clues})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def add_clue(request):
    if request.method == 'POST':
        form = ClueForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Clue added successfully.')
            return redirect('clue_list')
    else:
        form = ClueForm()
    return render(request, 'clues/clue_form.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def edit_clue(request, clue_id):
    clue = get_object_or_404(Clue, pk=clue_id)
    if request.method == 'POST':
        form = ClueForm(request.POST, instance=clue)
        if form.is_valid():
            form.save()
            messages.success(request, 'Clue updated successfully.')
            return redirect('clue_list')
    else:
        form = ClueForm(instance=clue)
    return render(request, 'clues/clue_form.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_clue(request, clue_id):
    clue = get_object_or_404(Clue, pk=clue_id)
    if request.method == 'POST':
        clue.delete()
        messages.success(request, 'Clue deleted successfully.')
        return redirect('clue_list')
    return render(request, 'clues/clue_confirm_delete.html', {'clue': clue})

# hunts
@login_required
@user_passes_test(lambda u: u.is_superuser)
def hunt_list(request):
    hunts = Hunt.objects.all()
    return render(request, 'hunts/hunt_list.html', {'hunts': hunts})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def add_hunt(request):
    if request.method == 'POST':
        form = HuntForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Hunt added successfully.')
            return redirect('hunt_list')
    else:
        form = HuntForm()
    return render(request, 'hunts/hunt_form.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def edit_hunt(request, hunt_id):
    hunt = get_object_or_404(Hunt, pk=hunt_id)
    if request.method == 'POST':
        form = HuntForm(request.POST, instance=hunt)
        if form.is_valid():
            form.save()
            messages.success(request, 'Hunt updated successfully.')
            return redirect('hunt_list')
    else:
        form = HuntForm(instance=hunt)
    return render(request, 'hunts/hunt_form.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_hunt(request, hunt_id):
    hunt = get_object_or_404(Hunt, pk=hunt_id)
    if request.method == 'POST':
        hunt.delete()
        messages.success(request, 'Hunt deleted successfully.')
        return redirect('hunt_list')
    return render(request, 'hunts/hunt_confirm_delete.html', {'hunt': hunt})