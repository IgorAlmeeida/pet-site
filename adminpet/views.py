from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from .forms import (ProjectForm, 
                    CronogramForm, 
                    ActivityForm, 
                    CategoryForm, 
                    PostForm, 
                    UserForm, 
                    ProfileForm, 
                    ReunionForm)
from .models import Project, Cronogram, Activity, Profile, Reunion
from website.models import Category, Post
from django.conf import settings
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required()
def home (request):
    return render(request,'adminpet/index.html')
    
def forgotPassword(request):
    return render(request,'adminpet/forgot-password.html')

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    
    return render(request,'adminpet/register.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

def login(request):
    data = {}
    mensagem = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                auth_login(request, user)
                return redirect('page_home')
            else:
                mensagem = ("Sua conta está inativa.")
        else:
            mensagem = ("Dados de login inválidos.")
    data['mensagem'] = mensagem
    return render(request, 'adminpet/login.html', data)

@login_required
def user_logout(request):
    logout(request)
    return redirect('page_home_website')


#------------------------------------VIEWS PROJECT-----------------------------------------#
@login_required()
def listProjects(request):

    search = request.GET.get("search")

    projects_list = []

    if (search):
        projects_list = Project.objects.filter(title__icontains = search)
    else: 
        projects_list = Project.objects.all()

    paginator = Paginator(list(projects_list), 10)

    page = request.GET.get("page")

    projects = paginator.get_page(page)

    data = {}
    data['objects'] = projects
    data['paginator'] = paginator
    return render(request, 'adminpet/project/list_project.html', data)

@login_required()
def listMyProjects(request):
    return render(request, 'adminpet/project/list_my_projects.html')

@login_required()
def newProject(request):
    form = ProjectForm(request.POST or None)

    if(request.method == 'POST'):
        if(form.is_valid()):
            form.save()
            return redirect('list_project')
    else:
        formProject = ProjectForm()
        data = {'form_project': formProject}
        return render(request, 'adminpet/project/new_project.html', data)

@login_required()
def updateProject(request, id):
    data ={}
    project = Project.objects.get(id=id)
    formProject = ProjectForm(request.POST or None, instance=project)

    data['project'] = project
    data['form_project'] = formProject 

    if (request.method == 'POST'):
        if (formProject.is_valid()):
            formProject.save()
            return redirect('list_project')
    else:
        return render(request, 'adminpet/project/update_project.html', data)

@login_required()
def deleteProject(request, id):
    project = Project.objects.get(id=id) or None
    if (request.method == 'POST'):
        if (project != None):
            project.delete()
            return redirect ('list_project')
        else:
            data = {}
            mensagem = ("Projeto não encontrado.")
            data['mensagem'] = mensagem
            return render(request, 'adminpet/project/delete_project.html', data)

    else:
        data = {}
        data['project'] = project
        return render(request, 'adminpet/project/delete_project.html', data)

@login_required()
def detailProject(request, id):
    data = {}
    project = Project.objects.get(id=id or None)
    if (project == None):
        mensagem = ("Não foi possível encontrar o projeto no banco de dados")
        data['mensagem'] = mensagem
        return render('adminpet/project/show_project.html', data)
    else:
        data['project'] = project
        return render(request, 'adminpet/project/show_project.html', data)


#----------------------------------------VIEWS CRONOGRAM---------------------------------------#
@login_required()
def newCronogramProject(request, idProject):
    formCronogram = CronogramForm(request.POST or None)

    if(request.method == 'POST'):
        
        if(formCronogram.is_valid()):
            formCronogram.save()
            return redirect('list_project')

    else:
        #Customing Forms
        project = Project.objects.get(id=idProject)
        formCronogram = CronogramForm()
        formCronogram.fields["project"].initial = project.id
        
        data = {'form_cronogram': formCronogram, 'project':project}

        return render(request, 'adminpet/cronogram/new_cronogram.html', data)

@login_required()
def updateCronogramProject(request, idProject, idCronogram):
    data ={}
    project = Project.objects.get(id=idProject)
    cronogram = Cronogram.objects.get(id=idCronogram)

    formCronogram = CronogramForm(request.POST or None, instance=cronogram)

    data['project'] = project
    data['cronogram'] = cronogram
    data['form_cronogram'] = formCronogram 

    if (request.method == 'POST'):
        if (formCronogram.is_valid()):
            formCronogram.save()
            return redirect('list_project')
    else:
        return render(request, 'adminpet/cronogram/update_cronogram.html', data)

@login_required()
def deleteCronogramProject(request, idProject, idCronogram):
    cronogram = Cronogram.objects.get(id=idCronogram)
    project = Project.objects.get(id=idProject)

    if (request.method == 'POST'):
        if (project != None):
            cronogram.delete()
            return redirect ('list_cronogram', idProject=project.id)
        else:
            data = {}
            mensagem = ("Cronograma não encontrado.")
            data['mensagem'] = mensagem
            return render(request, 'adminpet/project/list_project.html', data)

    else:
        data = {}
        data['project'] = project
        data['cronogram'] = cronogram
        return render(request, 'adminpet/cronogram/delete_cronogram.html', data)

@login_required()
def listCronogramProject(request, idProject):

    search = request.GET.get("search")
    project = Project.objects.get(id=idProject)

    cronogram_list = []

    if (search):
        cronogram_list = Cronogram.objects.filter(project_id=idProject,title__icontains = search)
    else: 
        cronogram_list = Cronogram.objects.filter(project_id=idProject)

    paginator = Paginator(list(cronogram_list),20)

    page = request.GET.get("page")

    cronograms = paginator.get_page(page)

    data = {}
    data['project'] = project
    data['objects'] = cronograms
    data['paginator'] = paginator
    return render(request, 'adminpet/cronogram/list_cronogram.html', data)


#----------------------------------------VIEWS ACTIVITY---------------------------------------#

@login_required()
def newActivityProject(request, idProject):
    formActivity = ActivityForm(request.POST or None)

    if(request.method == 'POST'):
        
        if(formActivity.is_valid()):
            formActivity.save()
            return redirect('list_activity', idProject=idProject)

    else:
        #Customing Forms
        project = Project.objects.get(id=idProject)
        formActivity = ActivityForm()
        formActivity.fields["project"].initial = project.id
        
        data = {'form_activity': formActivity, 'project':project}

        return render(request, 'adminpet/activity/new_activity.html', data)

@login_required()
def updateActivityProject(request, idProject, idActivity):
    data ={}
    project = Project.objects.get(id=idProject)
    activity = Activity.objects.get(id=idActivity)

    formActivity = ActivityForm(request.POST or None, instance=activity)

    data['project'] = project
    data['activity'] = activity
    data['form_activity'] = formActivity 

    if (request.method == 'POST'):
        if (formActivity.is_valid()):
            formActivity.save()
            return redirect('list_activity', idProject=idProject)
    else:
        return render(request, 'adminpet/activity/update_activity.html', data)

@login_required()
def deleteActivityProject(request, idProject, idActivity):
    activity = Activity.objects.get(id=idActivity)
    project = Project.objects.get(id=idProject)

    if (request.method == 'POST'):
        if (project != None):
            activity.delete()
            return redirect ('list_activity', idProject=project.id)
        else:
            data = {}
            mensagem = ("Atividade não encontrado.")
            data['mensagem'] = mensagem
            return render(request, 'adminpet/activity/list_activity.html', data)

    else:
        data = {}
        data['project'] = project
        data['activity'] = activity
        return render(request, 'adminpet/activity/delete_activity.html', data)

@login_required()
def listActivityProject(request, idProject):

    search = request.GET.get("search")
    project = Project.objects.get(id=idProject)

    activity_list = []

    if (search):
        activity_list = Activity.objects.filter(project_id=idProject,title__icontains = search)
    else: 
        activity_list = Activity.objects.filter(project_id=idProject)

    paginator = Paginator(list(activity_list), 10)

    page = request.GET.get("page")

    activitys = paginator.get_page(page)

    data = {}
    data['project'] = project
    data['objects'] = activitys
    data['paginator'] = paginator

    return render(request, 'adminpet/activity/list_activity.html', data)

# --------------------------------Blog----------------------------------------------------
@login_required()
def newCategory(request):
    form = CategoryForm(request.POST or None)

    if(request.method == 'POST'):
        if(form.is_valid()):
            form.save()
            return redirect('list_category')
    else:
        form = CategoryForm()
        data = {'form_category': form}
        return render(request, 'adminpet/category/new_category.html', data)

@login_required()
def updateCategory(request, idCategory):
    data ={}
    category = Category.objects.get(id=idCategory)
    formCategory = CategoryForm(request.POST or None, instance=category)

    data['category'] = category
    data['form_category'] = formCategory 

    if (request.method == 'POST'):
        if (formCategory.is_valid()):
            formCategory.save()
            return redirect('list_category')
    else:
        return render(request, 'adminpet/category/update_category.html', data)

@login_required()
def listCategory(request):

    search = request.GET.get("search")
    project = Project.objects.get(id=idProject)

    category_list = []

    if (search):
        category_list = Category.objects.filter(project_id=idProject,title__icontains = search)
    else: 
        category_list = Category.objects.filter(project_id=idProject)

    paginator = Paginator(list(category_list), 10)

    page = request.GET.get("page")

    categorys = paginator.get_page(page)

    data = {}
    data['objects'] =  categorys
    data['paginator'] = paginator
    return render(request, 'adminpet/category/list_category.html', data)

@login_required()
def deleteCategory(request, idCategory):
    category = Category.objects.get(id=idCategory) or None

    if (request.method == 'POST'):
        if (category != None):
            category.delete()
            return redirect ('list_category')
        else:
            data = {}
            mensagem = ("Projeto não encontrado.")
            data['mensagem'] = mensagem
            return render(request, 'adminpet/category/delete_post.html', data)

    else:
        data = {}
        data['category'] = category
        return render(request, 'adminpet/category/delete_category.html', data)

@login_required()
def newPost(request):
    form = PostForm(request.POST or None)
    
    if(request.method == 'POST'):
        if(form.is_valid()):
            form.save()
            return redirect('list_post')
    else:
        formPost = PostForm()
        profile = Profile.objects.get(user_id=request.user.id)
        formPost.fields["creator"].initial = profile.id
        data = {'form_post': formPost}
        return render(request, 'adminpet/post/new_post.html', data)
    
@login_required()
def updatePost(request, idPost):
    data ={}
    post = Post.objects.get(id=idPost)
    formPost = PostForm(request.POST or None, instance=post)

    data['post'] = post
    data['form_post'] = formPost 

    if (request.method == 'POST'):
        if (formPost.is_valid()):
            formPost.save()
            return redirect('list_post')
    else:
        return render(request, 'adminpet/post/update_post.html', data)

@login_required()
def listPost(request):

    search = request.GET.get("search")

    post_list = []

    if (search):
        post_list = Post.objects.filter(title__icontains = search)
    else: 
        post_list = Post.objects.all()
    
    paginator = Paginator(list(post_list),10)

    page = request.GET.get("page")

    posts = paginator.get_page(page)

    data = {}
    data['objects'] = posts
    data['paginator'] = paginator
    return render(request, 'adminpet/post/list_post.html', data)

@login_required()  
def detailPost(request, idPost):
    data = {}
    post = Post.objects.get(id=idPost or None)
    if (post == None):
        mensagem = ("Não foi possível encontrar o projeto no banco de dados")
        data['mensagem'] = mensagem
        return render(request, 'adminpet/post/show_post.html', data)
    else:
        data['post'] = post
        return render(request, 'adminpet/post/show_post.html', data)

@login_required()
def deletePost(request, idPost):
    data = {}
    post = Post.objects.get(id=idPost or None)
    if request.method == "POST":
        if (post == None):
            mensagem = ("Não foi possível encontrar o projeto no banco de dados")
            data['mensagem'] = mensagem
            return render(request, 'adminpet/post/delete_post.html', data)
        else:
            post.delete()
            redirect('list_post')
    else:
        data['post'] = post
        return render(request, 'adminpet/post/delete_post.html', data)


@login_required()
def createReunion(request):
    form = ReunionForm(request.POST or None)
    
    if(request.method == 'POST'):
        if(form.is_valid()):
            form.save()
            return redirect('list_reunion')
    else:
        form = ReunionForm()
        data = {'form_reunion': form}
        return render(request, 'adminpet/reunion/new_reunion.html', data)

@login_required()
def updateReunion(request, idReunion):
    data ={}
    reunion = Reunion.objects.get(id=idReunion)
    form = ReunionForm(request.POST or None, instance=reunion)

    data['reunion'] = reunion
    data['form_reunion'] = form

    if (request.method == 'POST'):
        if (form.is_valid()):
            form.save()
            return redirect('list_reunion')
    else:
        return render(request, 'adminpet/reunion/update_reunion.html', data)

@login_required()
def listReunion(request):
    search = request.GET.get("search")

    reunion_list = []

    if (search):
        reunion_list = Reunion.objects.filter(title__icontains = search)
    else: 
        reunion_list = Reunion.objects.all()
    
    paginator = Paginator(list(reunion_list),10)

    page = request.GET.get("page")

    posts = paginator.get_page(page)

    data = {}
    data['objects'] = posts
    data['paginator'] = paginator
    return render(request, 'adminpet/reunion/list_reunion.html', data)

@login_required()
def deleteReunion(request, idReunion):
    data = {}
    reunion = Reunion.objects.get(id=idReunion or None)
    if request.method == "POST":
        if (reunion == None):
            mensagem = ("Não foi possível encontrar o projeto no banco de dados")
            data['mensagem'] = mensagem
            data['reunion'] = reunion
            return render(request, 'adminpet/reunion/delete_reunion.html', data)
        else:
            reunion.delete()
            return redirect('list_reunion')
    else:
        data['reunion'] = reunion
        return render(request, 'adminpet/reunion/delete_reunion.html', data)

