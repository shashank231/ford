from dataclasses import fields
from typing import OrderedDict
import django_filters
from . models import *

class employeefilter(django_filters.FilterSet):
    class Meta:
        model = employee
        fields = "__all__"