# projects/views.py

# Django modules
from django.shortcuts import render, redirect

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
    
    # 1. Load ProjectForm class
    form = ProjectForm()

    # Jika ada POST request, proses formnya
    if request.method == "POST":

        # # Tesing the form: isi form lalu submit
        # print(request.POST) # tested :)

        # 2. Instantiate the ProjectForm class
        form = ProjectForm(request.POST)

        # 3. Save the input if form input valid
        if form.is_valid():
            form.save()
            return redirect('projects:projects')

    # 4. Context dictionary
    context = {
        'form':form,
    } 

    # Template
    return render(request, 'projects/project_form.html', context) # 5. Render context


