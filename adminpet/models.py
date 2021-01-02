from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField 

# Create your models here.

class Profile(models.Model):
    SEXO_CHOICES = (
        ("Feminino", "Feminino"),
        ("Masculino", "Masculino"),
    )

    TYPE_USER = (
        ("Tutor", "Tutor"),
        ("Petiano", "Petiano"),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    completeName = models.CharField(max_length=150, blank=False, null=False)
    sexo = models.CharField(max_length=20, blank=False, null=False, choices=SEXO_CHOICES)
    cpf = models.CharField(max_length=11, blank=False, null=False)
    ancientDate = models.DateField(blank=False, null=False, auto_now=False)
    typeUser = models.CharField(max_length=20, blank=False, null=False, choices=TYPE_USER, default="Petiano")
    active = models.BooleanField(blank=False, null=False, default=True)

    def __str__(self):
        return str(self.user.username)

class Project(models.Model):

    STATUS = (
        ("Ativo", "Ativo"),
        ("Inativo", "Inativo"),
    )
    
    title = models.CharField(max_length=200, blank=False, null=False)
    introduction = RichTextField(blank=False, null=False)
    justification = RichTextField(blank=False, null=False)
    objective =  RichTextField(blank=False, null=False)
    methodology = RichTextField(blank=False, null=False)
    creators = models.ManyToManyField(Profile)
    reference = RichTextField(blank=False, null=False)
    createDate = models.DateField(blank=False, null=False, auto_now=True)
    status = models.CharField(max_length=20, blank=False, null=False, choices=STATUS, default="Ativo")

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
        ("Ordinária", "Ordinária"),
        ("Extraórdinária", "Extraórdinária"),
    )
    title = models.CharField(max_length=50, blank=False, null=False)
    present = models.ManyToManyField(Profile)
    ata = models.TextField()
    dateReunion = models.DateField(blank=False, null=False)
    typeReunion = models.CharField(max_length=20, choices=TYPE_REUNION, default='Ordinária', blank=False, null=False)
 
    