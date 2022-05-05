from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from . models import *


class employeeform(ModelForm):
    class Meta:
        model = employee
        fields = "__all__"

class typeform(ModelForm):
    class Meta:
        model = type
        fields = "__all__"

class laptopform(ModelForm):
    class Meta:
        model = laptop
        fields = "__all__"

class orderform(ModelForm):
    class Meta:
        model = order
        fields = "__all__"

        

        
