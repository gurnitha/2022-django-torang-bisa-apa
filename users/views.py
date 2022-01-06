# users/views.py

# Django modules
from django.shortcuts import render

# Locals
from . models import Profile 

# Create your views here.

# Profile view
def profile_view(request):

	profiles = Profile.objects.all()
	context = {
		'profiles':profiles
	}

	return render(request, 'users/profile.html', context)