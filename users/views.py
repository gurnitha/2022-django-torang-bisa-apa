# users/views.py

# Django modules
from django.shortcuts import render

# Create your views here.

# Profile view
def profile_view(request):
	return render(request, 'users/profile.html')