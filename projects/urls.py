# projects/urls.py

# Django modules
from django.urls import path

# Locals
from projects import views

# Appname
app_name = 'projects'


urlpatterns = [
    path('', views.projects_view, name='projects'),
]
