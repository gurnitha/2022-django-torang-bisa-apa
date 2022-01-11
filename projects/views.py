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

    '''
    1. Agar bisa membuat proyek, user HARUS:
       - Sign up dan login
       - Kemudian dapatkan data profile dari user tsb.'''
    profile = request.user.profile

    # 2. Load ProjectForm class yg berasal dari forms.py.
    form = ProjectForm()

    # 3. Jika ada request dgn method POST, proses formnya.
    if request.method == "POST":

        # # Tesing the form: isi form lalu submit
        # print(request.POST) # tested :)

        ''' 
        4. Instantiate the ProjectForm class dengan parameter
           - request.POST, dan 
           - request.FILES
           * request.FILES dimaksudkan agar bisa mengupload image.'''
        form = ProjectForm(request.POST, request.FILES)

        # 5. Pastikan semua input pada form adalah valid.
        if form.is_valid():
            '''
            6. Ambil semua data dari form,
               tapi jangan langsung disimpan ke dalam db.'''
            project = form.save(commit=False)
            '''
            7. Update data owner dari proyek yg sdg dibuat.
               Data itu mempunya hub OneToMany dgn profile.'''
            project.owner = profile
            # 8. Lalu save data proyek ke dalam db.
            project.save()
            
            return redirect('projects:projects')

    # 9. Tempata semua data dari form ke dalam Context dictionary
    context = {
        'form':form,
    } 

    '''
    10. Sertakan context dictionary pada template 
        agar data dari form bisa ditampilan pada laman web.'''
    return render(request, 'projects/project_form.html', context)


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