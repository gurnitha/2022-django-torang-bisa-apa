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
    
    # Authentication
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),

    path('', views.profile_view, name='profiles'),
    path('profile/<str:pk>/', views.profile_user_view, name='profile_user'),

]
