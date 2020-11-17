from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def home (request):
    return render(request,'adminpet/index.html')

def list_projects(request):
    return ''

def new_project(request):
    return ''

def update_project(resquest, id):
    return ''

def delete_project(request, id):
    return ''

def list_my_projects(request):
    return ''
    