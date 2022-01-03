# projects/views.py

# Django modules
from django.shortcuts import render

# Create your views here.

# Static dictionary data
projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community'
    }
]


def projects_view(request):

    page_title = 'Projects'
    context = {
        'title':page_title,
        'projects':projectsList
    }

    return render(request, 'projects/projects.html', context)


def project_single_view(request):
    return render(request, 'projects/project_single.html')