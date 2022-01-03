# config/urls.py

# Django modules
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    
    # Projects
    path('', include('projects.urls', namespace='projects')),
    
    # Admin 
    path('admin/', admin.site.urls),
]
