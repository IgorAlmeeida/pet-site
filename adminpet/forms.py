from django.forms import ModelForm
from django import forms
from .models import Project, Cronogram, Activity, Profile, Reunion
from website.models import Category, Post
from django.contrib.auth.models import User

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        labels = {
            'title' : ('Título:'),
            'introduction' : ('Introdução:'),
            'justification' : ('Justificativa:'),
            'objective' : ('Objetivos:'),
            'methodology' : ('Metodologia:'),
            'creators' : ('Criadores:'),
            'reference' : ('Referências:'),
            'createDate' : ('Data de Criação:'),
            'status' : ('Status:'),
        }
        #help_texts = {'title': ('Digite o título do projeto'),}
        error_messages = {
            'title': {
                'max_length': ("O título digitado é muito longo"),
            },
        }

class CronogramForm(ModelForm):
    class Meta:
        model = Cronogram
        fields = '__all__'
        labels = {
            'title' : ('Título:'),
            'endDate' : ('Fim:'),
            'initDate' : ('Inicio:'),
            'project' : ('Projeto:'),
        }
        widgets = {
            'initDate': forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control','type': 'date'}),
            'endDate' : forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control','type': 'date'}),
            'project' : forms.HiddenInput(),
        }

class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = '__all__'
        labels = {
            'title': ('Titulo'),
            'description' : ('Descrição:'),
            'realizationDate' : ('Data:'),
            'project' : ('Projeto:'),
            'realizators' : ('Realizado por:'),
        }
        widgets = {
            'realizationDate': forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control','type': 'date'}),
            'project' : forms.HiddenInput(),
        }

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        labels = {
            'title' : ('Título'),
            'dateCreate' : ('Data de Criação'),
            'dateUpdated' : ('Ultima Atualização'),
            'body' : ('Texto'),
            'category' : ('Categoria'),
            'creator' : ('Criador'),
        }
        widgets = {
            'creator': forms.HiddenInput(),
        }
        


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        labels = {
            'name': ('Descrição'),
            'course': ('Curso')
        }
        widgets = {}


class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')
        labels = {
            'username': ('Usuário'),
            'password': ('Senha'),
            'email':('Email'),
        }


class ProfileForm(ModelForm):
    class Meta():
        model = Profile
        fields = ('completeName','cpf', 'sexo', 'ancientDate')
        labels = {
            'cpf': ('CPF'),
            'ancientDate': ('Data de Nascimento'),
            'sexo':('Sexo'),
            'completeName': ('Nome Completo')
        }
        widgets = {
            'ancientDate': forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control','type': 'date'}),
        }

class ReunionForm(ModelForm):
    class Meta():
        model = Reunion
        fields = ('title','present', 'ata', 'dateReunion')
        labels = {
            'title': ('Titulo'),
            'present': ('Presentes'),
            'ata':('Ata'),
            'dateReunion': ('Data')
        }
        widgets = {
            'ancientDate': forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control','type': 'date'}),
        }

