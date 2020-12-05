from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    SEXO_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino"),
    )

    TYPE_USER = (
        ("T", "Tutor"),
        ("P", "Petiano"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    completeName = models.CharField(max_length=150, blank=False, null=False)
    sexo = models.CharField(max_length=2, blank=False, null=False, choices=SEXO_CHOICES)
    cpf = models.CharField(max_length=11, blank=False, null=False)
    ancientDate = models.DateField(blank=False, null=False, auto_now=False)
    typeUser = models.CharField(max_length=2, blank=False, null=False, choices=TYPE_USER, default="P")
    active = models.BooleanField(blank=False, null=False, default=True)

    def __str__(self):
        return str(self.user.username)

class Project(models.Model):

    STATUS = (
        ("A", "Ativo"),
        ("I", "Inativo"),
    )
    
    title = models.CharField(max_length=200, blank=False, null=False)
    introduction = models.TextField(blank=False, null=False)
    justification = models.TextField(blank=False, null=False)
    objective =  models.TextField(blank=False, null=False)
    methodology = models.TextField(blank=False, null=False)
    creators = models.ManyToManyField(Profile)
    reference = models.TextField(blank=False, null=False)
    createDate = models.DateField(blank=False, null=False, auto_now=True)
    status = models.CharField(max_length=2, blank=False, null=False, choices=STATUS, default="A")

    def __str__(self):
        return str(self.title)

class Cronogram(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    initDate = models.DateField(blank=False, null=False, auto_now=False) 
    endDate = models.DateField(blank=False, null=False, auto_now=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)

class Activity(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=True, null=False)
    realizationDate = models.DateTimeField(blank=False, null=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    realizators = models.ManyToManyField(Profile)

    def __str__(self):
        return str(self.description)

class Reunion (models.Model):
    TYPE_REUNION = (
        ("O", "Ordinária"),
        ("E", "Extraórdinária"),
    )

    