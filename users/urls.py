# users/urls.py

# Django modules
from django.urls import path

# Locals
from . import views

# Appname
app_name = 'users'

urlpatterns = [
    
    # Authentication
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),

    path('users/', views.profile_view, name='profiles'),
    path('user/profile/<str:pk>/', views.profile_user_view, name='profile_user'),
]
