from django.db import models
from adminpet.models import Profile

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(sefl):
        return str(sefl.name)

class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    course = models.ManyToManyField(Course)

    def __str__(self):
        return str(self.name)

class Post(models.Model):
    title = models.CharField(max_length=300, blank=False, null=False)
    dateCreate = models.DateTimeField(auto_now=True, blank=False, null=False)
    dateUpdated = models.DateTimeField(auto_now= True)
    body = models.TextField(blank=False, null=False)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    creator = models.ForeignKey(Profile, on_delete=models.CASCADE) 

    def __str__(self):
        return str(self.title)

