# projects/views.py

# Django modules
from django.shortcuts import render

# Create your views here.

def projects_view(request):
	return render(request, 'projects/projects.html')


def project_single_view(request):
	return render(request, 'projects/project_single.html')