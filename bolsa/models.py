from django.db import models

# Create your models here.

class Person (models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    cpf = models.CharField(max_length=11, blank=False, null=False, unique=True)
    email = models.EmailField(blank=False, null=False, unique=True)
    hash_fnde = models.CharField(max_length=200, blank=False, null=False)

class Bag(models.Model):
    person = models.ForeignKey('Person', on_delete=models.CASCADE, default=None) 
    bag = models.CharField(max_length=50, blank=False, null=False)
    bank_order = models.CharField(max_length=50, blank=False, null=False)
    value = models.FloatField(blank=False, null=False)
    is_send = models.BooleanField(default=False, null=False, blank=False)
