from django.forms import ModelForm
from django import forms
from .models import Project, Cronogram


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
            'initDate' : ('Início:'),
            'endDate' : ('Fim:'),
            'project' : ('Projeto:'),
        }
