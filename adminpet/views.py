from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProjectForm, CronogramForm, ActivityForm
from .models import Project, Cronogram, Activity

# Create your views here.

def home (request):
    return render(request,'adminpet/index.html')

def login(request):
    return render(request,'adminpet/login.html')
def forgotPassword(request):
    return render(request,'adminpet/forgot-password.html')
def register(request):
    return render(request,'adminpet/register.html')    


#------------------------------------VIEWS PROJECT-----------------------------------------#
def listProjects(request):
    projects = Project.objects.all()
    data = {'projects': projects}
    return render(request, 'adminpet/project/list_project.html', data)

def listMyProjects(request):
    return render(request, 'adminpet/project/list_my_projects.html')

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

def listCronogramProject(request, idProject):
    project = Project.objects.get(id=idProject)
    cronograms = Cronogram.objects.filter(project_id=idProject)
    data = {}
    data['project'] = project
    data['cronograms'] = cronograms
    return render(request, 'adminpet/cronogram/list_cronogram.html', data)


#----------------------------------------VIEWS ACTIVITY---------------------------------------#

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

def listActivityProject(request, idProject):
    project = Project.objects.get(id=idProject)
    activitys = Activity.objects.filter(project_id=idProject)
    data = {}
    data['project'] = project
    data['activitys'] = activitys
    return render(request, 'adminpet/activity/list_activity.html', data)