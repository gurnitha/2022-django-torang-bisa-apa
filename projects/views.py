# projects/views.py

# Django modules
from django.shortcuts import render

# Create your views here.

def projects_view(request):
	message = 'Hai semuanya, apa kabar?'
	context = {'msg':message}
	return render(request, 'projects/projects.html', context)


def project_single_view(request):
	return render(request, 'projects/project_single.html')