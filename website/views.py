from django.shortcuts import render
from .models import Post

# Create your views here.

def home(request):

    return render(request, 'website/index.html')

def pageBlog(request):
    posts = Post.objects.all()
    data = {}
    data['posts'] = posts 
    return render(request, 'website/blog.html', data)

def pageMembers(request):
    return render(request, 'website/membros.html')
    
def pageSelections(request):
    return render(request, 'website/selecoes.html')
    
def pageContatus(request):
    return render(request, 'website/contato.html')

def pagePost(request, idPost):
    post = Post.objects.get(id=idPost)
    data = {}
    data['post'] = post
    return render(request, 'website/post.html', data)

def pageProject(request, idProject):
    return render(request, 'website/projetos.html')