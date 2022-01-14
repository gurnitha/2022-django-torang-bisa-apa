# users/views.py

# Django modules
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q  

# Locals
from . models import (
	Profile, 
	# Skill
	)
from projects.models import Tag 
from . forms import CustomUserCreationForm, ProfileForm, SkillForm
from .utils import searchProfiles

# Create your views here.

# -------------------Authentication -------------------

# registerUser view
def registerUser(request):

	page = 'register'
	# form = UserCreationForm
	form = CustomUserCreationForm
	
	# Logic to register user

	# 1. If the request is POST, then
	#    use UserCreationForm
	if request.method == 'POST':
		# form = UserCreationForm(request.POST)
		form = CustomUserCreationForm(request.POST)
		''' 
		2. Authenticate the form, 
		   get the user's instance,
		   create temporary data
		   and don't save right away,
		   modify the instances to lowercase
		   then save the instace.'''
		if form.is_valid():
			user = form.save(commit=False)
			user.username = user.username.lower()
			user.save()

			# Message
			messages.success(request, 'User account was successfully created!')

			# Automatically Log in user after signing up
			login(request, user)
			# return redirect('users:profiles')
			return redirect('users:account_edit')

		# 3. If register faild
		else:
			messages.success(request, 'An error occurred during registration!')

	context = {
		'page':page,
		'form':form}
	
	return render(request, 'users/auth/register_login.html', context)


# loginUser view
def loginUser(request):

	# Don't show logn page to LOGGED IN user or
	# redirect logged in user to profiles page
	if request.user.is_authenticated:
		return redirect('users:profiles')

	# 1. If POST request, get the input data
	#    that is the username and password
	if request.method == 'POST':
		# (Optional) Print out the input in the terminal
		# print(request.POST)

		username = request.POST['username']
		password = request.POST['password']

		# 2. Use 'try block' to check if the input data exist 
		# or not in the db, then return user
		try:
			user = User.objects.get(username=username)
		# 3. If user does not exist in db
		#    or the credentials is not correct
		#    show flash message
		except:
			messages.error(request, 'Username does not exitst!')

		# 4. If user exists, authenticate it, then return user
		user = authenticate(
			request,
			username=username,
			password=password)

		# 5. If authenticated (user does exist), log the user in
		# and redirect him to any page you want
		if user is not None:
			# This login will create session in the db
			# and the session will use it in the browser
			login(request, user)
			return redirect('users:profiles')

		# 6. If user exist, but its credentials incorrect
		else:
			messages.error(request, 'Username OR password is incorrect. Try it again ...')
			return redirect('users:login')


		''' NOTE:
			If username and password NOT CORRECT it will show messages like this:
			---------
			Username does not exitst!
			Username OR password is incorrect. Try it again ... 
			---------
		'''
	
	return render(request, 'users/auth/register_login.html')


# logoutUser view
def logoutUser(request):
	# Kill the session using the logout method
	# and redirect user to login page
	logout(request)
	# messages.error(request, 'User was logged out!')
	messages.info(request, 'Your are logged out!')
	return redirect('users:login')
	
# -------------------END Authentication ---------------



# Profile view
def profile_view(request):

	# Step 7 Search: use the searchProfiles method
	profiles, search_query = searchProfiles(request)

	# skills = Skill.objects.all()
	
	context = {
		'profiles':profiles,
		# 'skills': skills,
		'search_query':search_query
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


# Account user view
def account_user_view(request):
	profile = request.user.profile
	skills = profile.skill_set.all()
	# projects = profile.project_set.all()
	projects = profile.project_set.all()
	# print(projects)
	context = {
		'profile':profile,
		'skills':skills,
		'projects':projects
	}
	return render(request, 'users/account.html', context)


# editAccount view
def account_user_edit_view(request):

	# Get the profile from user
	profile = request.user.profile	

	# Get the attributes from the Profile model
	form = ProfileForm(instance=profile)	

	# If request mothod is POST, process the form
	if request.method == 'POST':
		form = ProfileForm(
					request.POST,
					request.FILES,
					instance=profile)

		# Use is_valid method to check if the form is valid,
		# if the form valid, then save it
		if form.is_valid():
			form.save()

		# Redirect to its account after saving
		return redirect('users:account')

	context = {
		'form':form
	}
	
	return render(request, 'users/profile_form.html', context)



# ---------------------------CRUD SKILL-----------------------

# createSkill view
def skill_create_view(request):

    '''
    1. Agar bisa membuat skill, user HARUS:
       - Sign up dan login
       - Kemudian dapatkan data profile dari user tsb.'''
    profile = request.user.profile

    # 2. Load SkillForm model yang diimport dari users/forms.py.
    form = SkillForm()

    # 3. Jika ada request dgn method POST, proses formnya.
    if request.method == "POST":

        # # Tesing the form: isi form lalu submit
        # print(request.POST) # tested :)

        ''' 
        4. Instantiate the SkillForm model dengan 
           parameter request.POST'''
        form = SkillForm(request.POST)

        # 5. Pastikan semua input pada form adalah valid.
        if form.is_valid():
            '''
            6. Ambil semua data dari form,
               tapi jangan langsung disimpan ke dalam db.'''
            skill = form.save(commit=False)
            '''
            7. Update data owner dari profile.
               Data itu mempunya hub OneToMany dgn skill.'''
            skill.owner = profile

            # 8. Lalu save data proyek ke dalam db.
            skill.save()

            # 9 Tampilkan pesan sukses
            messages.success(request, 'Skill was added successfully.')
            # 10. Arahkan user ke laman account
            return redirect('users:account')  

    # 11. Tempatkan semua data dari skill_form ke dalam Context dictionary
    context = {
    	'form':form
    }

    '''
    12. Sertakan context dictionary pada template 
        agar data dari skill_form bisa ditampilan pada laman web.'''   
    return render(request, 'users/skill_form.html', context)


# updateSkill view
def skill_update_view(request, pk):

    # Membuat variable page
    page = 'update'

    '''
    1. Agar bisa mengupdate skill, user HARUS:
       - login
       - Kemudian dapatkan profile dari user tsb.
       - User dan skill mempunyai hub. OneToOne.'''
    profile = request.user.profile

    '''
    2. Ambil id dari skill yg dimiliki oleh user tsb
       yg akan diupdate.
    '''
    skill = profile.skill_set.get(id=pk)

    ''' 
    3. Load SkillForm model yg berasal dari forms.py
       dgn parameter dari skill yg akan diupdate.
    '''
    form = SkillForm(instance=skill)

    # 4. Jika ada request dgn method POST, proses formnya.
    if request.method == "POST":

        # Tesing the form: fillin the form and submit it
        # print(request.POST) # tested :)

        ''' 
        5. Instantiate the SkillForm model dengan parameter
           - request.POST, dan
           - instance=skill.'''
        form = SkillForm(request.POST, instance=skill)

        # 6. Pastikan semua input pada form adalah valid.
        if form.is_valid():
            # 7. Lalu save data skill ke dalam db.
            skill.save()

            # 8. Tampilkan pesan sukses
            messages.success(request, 'Skill was updated successfully.')

			# 9. Arahkan user ke laman account
            return redirect('users:account')

    # 10. Tempatkan semua data dari form ke dalam Context dictionary
    context = {
        'form':form,
        'page':page
    }

    '''
    11. Sertakan context dictionary pada template 
        agar data dari form bisa ditampilan pada laman web.'''
    return render(request, 'users/skill_form.html', context)


# deleteSkill view
def skill_delete_view(request, pk):

    '''
    1. Untuk menghapus sebuah proyek, use HARUS'''
    profile = request.user.profile

	# 2. Ambil id dari skill yang akan dihapus
    skill = profile.skill_set.get(id=pk)

    '''
    3. Jika ada request dgn method POST
       gunakan method delete() untuk
       men-delete skill berdasarkan 
       instan yang diterima, tampilkan pesan
       sukses, lalu arahkan user
       kembali ke laman account.
    '''
    if request.method == 'POST':
        skill.delete()
        messages.success(request, 'Skill was deleted successfully.')
        return redirect('users:account')

    # 4. Tempatkan semua data dari form ke dalam Context dictionary
    context = {'object':skill}

    '''
    5. Sertakan context dictionary pada template 
        agar data dari form bisa ditampilan pada laman web.'''
    return render(request, 'users/skill_delete.html', context)

# ------------------------END CRUD SKILL----------------------
