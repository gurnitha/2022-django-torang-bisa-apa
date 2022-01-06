# users/admin.py

# Django modules
from django.contrib import admin

# Loclas
from users.models import Profile, Skill

# Register your models here.

admin.site.register(Profile) 
admin.site.register(Skill) 