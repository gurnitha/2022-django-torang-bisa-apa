# projects/forms.py

# Django modules
from django.forms import ModelForm

# Locals
from .models import Project

# Create your forms here.

# Naming the class: ModelName+Form
class ProjectForm(ModelForm):
	class Meta:
		model = Project
		fields = '__all__'
