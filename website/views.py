from django.shortcuts import render
from .models import Post
from adminpet.models import Project
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    data = {}
    data['projects'] = getProjects()
    data['posts'] = Post.objects.all().order_by('-id')[:10:1]
    return render(request, 'website/index.html', data)

def pageBlog(request):
    search = request.GET.get("search")

    posts_list = []

    if (search):
        posts_list = Post.objects.filter(title__icontains = search)
    else: 
        posts_list = Post.objects.all()

    paginator = Paginator(list(posts_list), 9)

    page = request.GET.get("page")

    posts = paginator.get_page(page)

    data = {}
    data['objects'] = posts
    data['paginator'] = paginator
    data['projects'] = getProjects()
    
    return render(request, 'website/blog.html', data)

def pageMembers(request):
    data = {}
    data['projects'] = getProjects()
    return render(request, 'website/membros.html', data)
    
def pageSelections(request):
    data = {}
    data['projects'] = getProjects()
    return render(request, 'website/selecoes.html', data)
    
def pageContatus(request):
    data = {}
    data['projects'] = getProjects()
    return render(request, 'website/contato.html', data)

def pagePost(request, idPost):
    post = Post.objects.get(id=idPost)

    data = {}
    data['post'] = post
    data['projects'] = getProjects()
    return render(request, 'website/post.html', data)

def pageProject(request, idProject):
    data = {}
    data['projects'] = getProjects()

    projectPage = Project.objects.get(id=idProject)
    data['projectPage'] = projectPage

    return render(request, 'website/projetos.html', data)

def getProjects():
    return Project.objects.all()
