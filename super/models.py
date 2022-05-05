
#from unicodedata import name
from operator import mod
from django.db import models

# Create your models here.

class employee(models.Model):
    name = models.CharField(max_length=200, null=True)
    eid = models.CharField(max_length=5, null=True)
    age = models.CharField(max_length=2, null=True)
    
    def __str__(self):
        return self.name

class type(models.Model):
    name = models.CharField(max_length=10, null=True)
    description = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class laptop(models.Model):
    company = models.CharField(max_length=50)
    sizee = models.CharField(max_length=20)
    price = models.CharField(max_length=10)

    def __str__(self):
        return self.company

class order(models.Model):
    num = models.CharField(max_length=5)
    emp = models.ForeignKey(employee, on_delete=models.CASCADE)
    lap = models.ForeignKey(laptop, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.num



