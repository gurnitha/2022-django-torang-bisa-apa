# projects/urls.py

# Django modules
from django.urls import path

# Locals
from projects import views

# Appname
app_name = 'projects'


urlpatterns = [
    path('', views.projects_view, name='projects'),
    path('single/<str:pk>/', views.project_single_view, name='project_single'),

    # CRUD
    path('create-project/', views.project_create_view, name='create_project'),
]
