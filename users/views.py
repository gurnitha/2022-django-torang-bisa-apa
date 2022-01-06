# users/views.py

# Django modules
from django.shortcuts import render

# Locals
from . models import Profile, Skill 

# Create your views here.

# Profile view
def profile_view(request):

	profiles = Profile.objects.all()
	skills = Skill.objects.all()
	
	context = {
		'profiles':profiles,
		'skills': skills
	}

	return render(request, 'users/profiles.html', context)


# Profile User view
def profile_user_view(request, pk):

	profile = Profile.objects.get(id=pk)
	
	context = {
		'profile':profile,
	}
	
	return render(request, 'users/profile_user.html', context)