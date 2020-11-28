from django.forms import ModelForm
from django import forms
from .models import Project, Cronogram, Activity
from website.models import Category, Post


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

