# users/urls.py

# Django modules
from django.urls import path

# Locals
from . import views

# Appname
app_name = 'users'

urlpatterns = [
    path('users/', views.profile_view, name='profiles'),
]
