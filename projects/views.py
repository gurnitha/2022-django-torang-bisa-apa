# projects/views.py

# Django modules
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# locals
from .models import Project
from .forms import ProjectForm
from .utils import searchProjects

# Create your views here.


def projects_view(request):

    # Step 5 Search: use the searchProfiles method
    projects, search_query = searchProjects(request)

    page = 1
    results = 3
    paginator = Paginator(projects, results)

    projects = paginator.page(page)

    # projects = Project.objects.all()
    page_title = 'Projects'
    
    context = {
        'title':page_title,
        'projects':projects,
        'search_query':search_query,
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

    '''
    1. Agar bisa mengupdate proyek, user HARUS:
       - login
       - Kemudian dapatkan profile dari user tsb.
       - User dan proyek mempunyai hub. OneToOne.'''
    profile = request.user.profile

    '''
    2. Ambil id dari proyek yg dimiliki oleh user tsb
       yg akan diupdate.
    '''
    project = Project.objects.get(id=pk)

    ''' 
    3. Load ProjectForm class yg berasal dari forms.py
       dgn parameter dari proyek yg akan diupdate.
    '''
    form = ProjectForm(instance=project)

    # 4. Jika ada request dgn method POST, proses formnya.
    if request.method == "POST":

        # Tesing the form: fillin the form and submit it
        # print(request.POST) # tested :)

        ''' 
        5. Instantiate the ProjectForm class dengan parameter
           - request.POST, 
           - request.FILES, dan
           - instance=project.'''
        form = ProjectForm(request.POST, request.FILES, instance=project)

        # 6. Pastikan semua input pada form adalah valid.
        if form.is_valid():
            # 7. Lalu save data proyek ke dalam db.
            project.save()
            
            # 8. Arahkan user ke laman proyek
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
def project_delete_view(request, pk):

    '''
    1. Untuk menghapus sebuah proyek, use HARUS
       - login.
       * user dan proyek memiliki hub
         OneToOne.'''
    profile = request.user.profile

    # 2. Ambil id dari proyek yang akan dihapus
    project = profile.project_set.get(id=pk)

    '''
    3. Jika ada request dgn method POST
       gunakan method delete() untuk
       men-delete proyek berdasarkan 
       instan yang diterima lalu arahkan
       kembali ke laman proyek.
    '''
    if request.method == "POST":
        project.delete()
        return redirect('projects:projects')

    # 4. Tempatkan semua data dari form ke dalam Context dictionary
    context = {'object':project}

    '''
    5. Sertakan context dictionary pada template 
        agar data dari form bisa ditampilan pada laman web.'''
    return render(request, 'projects/project_delete.html', context)
