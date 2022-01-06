# projects/urls.py

# Django modules
from django.urls import path

# Locals
from projects import views

# Appname
app_name = 'projects'


urlpatterns = [
    path('projects/', views.projects_view, name='projects'),
    path('project/<str:pk>/', views.project_single_view, name='project_single'),

    # CRUD
    path('create-project/', views.project_create_view, name='create_project'),
    path('update-project/<str:pk>/', views.project_update_view, name='update_project'),
    path('delete-project/<str:pk>/', views.project_delete_view, name='delete_project'),
]
