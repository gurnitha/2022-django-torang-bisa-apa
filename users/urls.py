# users/urls.py

# Django modules
from django.urls import path

# Locals
from . import views

# Appname
app_name = 'users'

urlpatterns = [

    # Account
    path('account/', views.account_user_view, name='account'),
    path('edit-account/', views.account_user_edit_view, name='account_edit'),

    # Authentication
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),

    path('', views.profile_view, name='profiles'),
    path('profile/<str:pk>/', views.profile_user_view, name='profile_user'),

    # Skill
    path('create-skill/', views.skill_create_view, name='skill_create'),
    path('update-skill/<str:pk>/', views.skill_update_view, name='skill_update'),
]