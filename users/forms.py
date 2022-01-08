# user/forms.py

# Django modules
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
	class Meta:
		model = User  
		fields = [
			'first_name', 'email', 
			'username', 'password1', 'password2']
		# Replacing 'First Name' to 'Name'
		labels = {'first_name': 'Name'}