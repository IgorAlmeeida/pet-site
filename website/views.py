from django.shortcuts import render
from .models import Post
from adminpet.models import Project
from django.core.paginator import Paginator
import requests
import json
from bolsa.models import Person
from django.http import JsonResponse


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
    
def pageBolsa(request):
    data = {}
    data['projects'] = getProjects()
    return render(request, 'website/bolsa.html', data)

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

def cadastrarPessoa(request):
    cpf = request.POST.get('cpf', None)  
    email = request.POST.get('email', None)

    try:
        if (cpf != None and cpf != '' and email != None and email != ''):
            dadosPessoa = requests.get("https://www.fnde.gov.br/digef/rs/spba/publica/pessoa/1/10/"+cpf)
            
            if (dadosPessoa.status_code != 200):
                raise Exception("Banco de dados do FNDE indisponível, por favor tente mais tarde!")
            
            try:
                dadosPessoa = json.loads(dadosPessoa.content)
                person = Person(name=dadosPessoa['pessoas'][0]['nome'], cpf=cpf, email=email, hash_fnde=dadosPessoa['pessoas'][0]['hash'])
                person.save()
            except Exception as e:
                raise Exception("Email ou CPF já cadastrados.")
            
            return JsonResponse({'status':'200', 'mensagem': 'Cadastro realizdo com sucesso.'})
        else: 
            raise Exception("Por favor, insira todos os dados.") 
    except Exception as e:
        return JsonResponse({'status':'400', 'mensagem': str(e)})


