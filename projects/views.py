# projects/views.py

# Django modules
from django.shortcuts import render

# Create your views here.

def projects_view(request):

	page_title = 'Projects'
	context = {
		'title':page_title,
		'projects':projectsList
	}

	return render(request, 'projects/projects.html', context)


def project_single_view(request):
	return render(request, 'projects/project_single.html')