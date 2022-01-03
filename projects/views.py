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

    projectObject = Project.objects.get(id=pk)

    tags = projectObject.tags.all()
    context = {
        'project':projectObject,
        'tags':tags,
    } 

    return render(request, 'projects/project_single.html', context)


