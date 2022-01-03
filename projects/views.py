# projects/views.py

# Django modules
from django.shortcuts import render

# locals
from .models import Project

# Create your views here.

# # Static dictionary data
# projectsList = [
#     {
#         'id': '1',
#         'title': 'Ecommerce Website',
#         'description': 'Fully functional ecommerce website',
#         'tags': 'Django 3 | Python 3'
#     },
#     {
#         'id': '2',
#         'title': 'Portfolio Website',
#         'description': 'A personal website to write articles and display work',
#         'tags': 'Django 4 | Django CMS'
#     },
#     {
#         'id': '3',
#         'title': 'Social Network',
#         'description': 'An open source project built by the community',
#         'tags': 'FastAPI'
#     }
# ]


def projects_view(request):

    projects = Project.objects.all()
    page_title = 'Projects'
    context = {
        'title':page_title,
        'projects':projects
    }

    return render(request, 'projects/projects.html', context)


def project_single_view(request, pk):

    projectObject = None

    for i in projectsList:
        if i['id'] == pk:
            projectObject = i 

    context = {'project':projectObject}

    return render(request, 'projects/project_single.html', context)

def project(request, pk):
    projctObj = None
    for i in projectsList:
        if i['id'] == pk: 
            projctObj = i
    # context = 

    return render(request, 'projects/single-project.html', {'project':projctObj})