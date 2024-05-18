#urls.py
"""
URL configuration for taskMgmt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# urls.py

from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import (
    task_list, add_task, edit_task, delete_task,
    register, profile, edit_profile, create_user,
    user_list, team_list, add_team, edit_team, home,
    add_location, location_list, edit_location, delete_location,
    hunt_list, add_hunt, edit_hunt, delete_hunt,
    clue_list, add_clue, edit_clue, delete_clue
)

urlpatterns = [
    path('', home, name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('admin/', admin.site.urls),
    path('admin/create_user/', views.create_user, name='create_user'),
    path('admin/user-list/', views.user_list, name='user_list'),
    path('teams/', views.team_list, name='team_list'),
    path('teams/add/', add_team, name='add_team'),
    path('teams/edit/<int:team_id>/', views.edit_team, name='edit_team'),
    path('task_list/', task_list, name='task_list'),
    path('tasks/add/', add_task, name='add_task'),
    path('tasks/edit/<int:task_id>/', edit_task, name='edit_task'),
    path('tasks/delete/<int:task_id>/', delete_task, name='delete_task'),
    path('locations/add/', add_location, name='add_location'),
    path('locations/', location_list, name='location_list'),
    path('locations/edit/<int:location_id>/', edit_location, name='edit_location'),
    path('locations/delete/<int:location_id>/', delete_location, name='delete_location'),
    path('hunts/', hunt_list, name='hunt_list'),
    path('hunts/add/', add_hunt, name='add_hunt'),
    path('hunts/edit/<int:hunt_id>/', edit_hunt, name='edit_hunt'),
    path('hunts/delete/<int:hunt_id>/', delete_hunt, name='delete_hunt'),
    path('clues/', clue_list, name='clue_list'),
    path('clues/add/', add_clue, name='add_clue'),
    path('clues/edit/<int:clue_id>/', edit_clue, name='edit_clue'),
    path('clues/delete/<int:clue_id>/', delete_clue, name='delete_clue'),
]