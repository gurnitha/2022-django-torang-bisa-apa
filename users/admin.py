# users/admin.py

# Django modules
from django.contrib import admin

# Loclas
from users.models import Profile

# Register your models here.

admin.site.register(Profile) 