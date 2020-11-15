from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TypeUser(models.Model):
    descriptionUserType = models.CharField(max_length=20, blank=True, null=True)

class Status(models.Model):
    descriptionStatus = models.CharField(max_length=100, blank=False, null=False)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=11, blank=False, null=False)
    ancientDate = models.DateField(blank=False, null=False, auto_now=False)
    typeUser = models.OneToOneField('TypeUser', on_delete=models.DO_NOTHING)
    active = models.BooleanField(blank=False, null=False)

class Project(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    introduction = models.TextField(blank=False, null=False)
    justification = models.TextField(blank=False, null=False)
    objective =  models.TextField(blank=False, null=False)
    methodology = models.TextField(blank=False, null=False)
    creators = models.ManyToManyField('Profile')
    reference = models.TextField(blank=False, null=False)
    createDate = models.DateField(blank=False, null=False, auto_now=True)
    status = models.OneToOneField('Status', on_delete=models.DO_NOTHING)

class Cronogram(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    initDate = models.DateField(blank=False, null=False, auto_now=False) 
    endDate = models.DateField(blank=False, null=False, auto_now=False)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)

class Activity(models.Model):
    description = models.CharField(max_length=300, blank=True, null=True)
    realizationDate = models.DateTimeField(blank=False, null=False, auto_now=True)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    realizators = models.ManyToManyField('Profile')

