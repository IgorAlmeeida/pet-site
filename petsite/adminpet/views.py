from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProjectForm
from .models import Project

# Create your views here.

def home (request):
    return render(request,'adminpet/index.html')

def listProjects(request):
    projects = Project.objects.all()
    data = {'projects': projects}
    return render(request, 'adminpet/list_project.html', data)

def listMyProjects(request):
    return render(request, 'adminpet/list_my_projects.html')

def newProject(request):
    form = ProjectForm(request.POST or None)

    if(request.method == 'POST'):
        if(form.is_valid()):
            form.save()
            return redirect('list_project')
    else:
        formProject = ProjectForm()
        data = {'form_project': formProject}
        return render(request, 'adminpet/new_project.html', data)

def updateProject(resquest, id):
    render(request, 'adminpet/update_project.html')

def deleteProject(request, id):
    render(request, 'adminpet/delete_project.html')

    