from contextlib import redirect_stderr
from multiprocessing import context
import re

from django.shortcuts import render, redirect
from django.http import HttpResponse

from . models import employee, type, laptop
from . forms import employeeform, orderform, typeform, laptopform, orderform
from . filters import employeefilter

def home(request):
    employees = employee.objects.all()
    context = {"employees": employees}
    return render(request, "super/home.html", context)

def addtype(request):
    f2 = typeform()
    if request.method == 'POST':
        f2 = typeform(request.POST)
        if f2.is_valid:
            f2.save()
            return redirect('/about')
    context = {'f2': f2}
    return render(request, "super/addtype.html", context)

def about(request):
    types = type.objects.all()
    context = {'types': types}
    return render(request, "super/about.html", context)

def add(request):
    f1 = employeeform()
    if request.method == 'POST':
        # jo user ne add.html me enter kia vo form csrf token me ab view me a gaya hai
        f1 = employeeform(request.POST)
        if f1.is_valid:
            f1.save()
            return redirect('/')

    context = {'f1': f1}
    return render(request, "super/add.html", context)

def update(request, pk):
    emp = employee.objects.get(id=pk)
    f1 = employeeform(instance=emp)

    if request.method == 'POST':
        f1 = employeeform(request.POST, instance=emp)
        if f1.is_valid:
            f1.save()
            return redirect('/')

    context = {'f1': f1}
    return render(request, "super/add.html", context)

def delete(request, pk):
    emp = employee.objects.get(id=pk)

    if request.method == "POST":
        emp.delete()
        return redirect('/')

    context = {"emp": emp}
    return render(request, "super/delete.html", context)

def profile(request, pk):
    emp = employee.objects.get(id=pk)
    context = {"emp": emp}
    return render(request, "super/profile.html", context)

def search(request):
    mfi = employeefilter()

    emp11 = employee.objects.all()
    mf1 = employeefilter(request.GET, queryset=emp11)
    print("----------------")
    print()
    print()
    emp1 = mf1.qs
    print(emp1)

    context = {"mfi": mfi, "emp1": emp1}
    return render(request, "super/search.html", context)

def order(request):
    l1 = laptop.objects.all()
    f3 = orderform()

    if request.method == 'POST':
        f3 = orderform(request.POST)
        if f3.is_valid:
            f3.save()
            return redirect('/order')

    context = {'l1' :l1, 'f3': f3}
    return render(request, 'super/order.html', context)

def addlaptop(request):
    f2 = laptopform()
    if request.method == 'POST':
        f2 = laptopform(request.POST)
        if f2.is_valid:
            f2.save()
            return redirect('/order')
    
    context = {'f2' : f2}
    return render(request, 'super/addlaptop.html', context)


