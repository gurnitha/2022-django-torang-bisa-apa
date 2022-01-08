# projects/views.py

# Django modules
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

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
    

@login_required(login_url="users:login")
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


@login_required(login_url="users:login")
def project_update_view(request, pk):

    # 1. Get the project instance by its id
    project = Project.objects.get(id=pk)

    ''' 
    2. Instantiate the ProjectForm class
       with parameter the instance of the project.
    '''
    form = ProjectForm(instance=project)

    # 3. If there is POST request, process the form
    if request.method == "POST":

        # Tesing the form: fillin the form and submit it
        # print(request.POST) # tested :)

        # 4. Instantiate the ProjectForm class
        form = ProjectForm(request.POST, instance=project)
        
        # 5. Save input jika form input valid
        if form.is_valid():
            form.save()
            return redirect('projects:projects')

    # 6. Context dictionary
    context = {
        'form':form,
    } 

    # Template
    return render(request, 'projects/project_form.html', context) # 7. Render context



@login_required(login_url="users:login")
def project_delete_view(request, pk):

    # 1. Get the project instance by its id
    project = Project.objects.get(id=pk)

    '''
    2. Jika ada request dgn method POST
       gunakan method delete() untuk
       men-delete proyek berdasarkan 
       instan yang diterima lalu arahkan
       kembali ke halaman proyek.
    '''
    if request.method == "POST":
        project.delete()
        return redirect('projects:projects')

    context = {'object':project}
    
    return render(request, 'projects/project_delete.html', context)