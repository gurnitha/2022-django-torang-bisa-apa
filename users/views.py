# users/views.py

# Django modules
from django.shortcuts import render

# Locals
from . models import Profile, Skill
from projects.models import Tag 

# Create your views here.

# -------------------Authentication -------------------

# loginUser view
def loginUser(request):
	
	# Cek jika ada request dengan method POST
	if request.method == 'POST':
		# Print out the input in the terminal
		print(request.POST)

	return render(request, 'users/auth/register_login.html')

# -------------------END Authentication ---------------



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

	'''Get skill yg ada deskripsinya'''
	topSkills = profile.skill_set.exclude(description__exact="")

	'''Get skill tidak ada deskripsinya'''
	otherSkills = profile.skill_set.filter(description="")

	tags = Tag.objects.all()

	context = {
		'profile':profile,
		'topSkills':topSkills,
		'otherSkills':otherSkills,
		'tags':tags
	}
	
	return render(request, 'users/profile_user.html', context)
