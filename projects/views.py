# projects/views.py

# Django modules
from django.shortcuts import render

# locals
from .models import Project
from .forms import ProjectForm

# Create your views here.

def projects_view(request):

    projects = Project.objects.all()
    page_title = 'Projects'
    context = {
        'title':page_title,
        'projects':projects
    }

    return render(request, 'projects/projects.html', context)


def project_single_view(request, pk):

    projectObject = Project.objects.get(id=pk)

    tags = projectObject.tags.all()
    context = {
        'project':projectObject,
        'tags':tags,
    } 

    return render(request, 'projects/project_single.html', context)
    


def project_create_view(request):
    
    form = ProjectForm()

    context = {
        'form':form
    } 

    return render(request, 'projects/project_form.html', context)

