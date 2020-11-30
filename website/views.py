from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'website/index.html')

def pageBlog(request): 
    return render(request, 'website/blog.html')

def pageMembers(request):
    return render(request, 'website/membros.html')
    
def pageSelections(request):
    return render(request, 'website/selecoes.html')
    
def pageContatus(request):
    return render(request, 'website/contato.html')

def pagePost(request, idPost):
    return render(request, 'website/post.html')

def pageProject(request, idProject):
    return render(request, 'website/projetos.html')