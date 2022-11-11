from django.shortcuts import render, redirect
from .models import Employee
# Create your views here.
from .forms import Empinfo
def empviews(request):
    employee=Employee.objects.all()
    return render(request,"testapp/index.html",{"employee":employee})

def insert(request):
    form=Empinfo()
    if request.method=="POST":
        form = Empinfo(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return redirect("/")
    return render(request,"testapp/insert.html",{"form":form})


def delete(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()
    return redirect("/")
def update(request,id):
    employee=Employee.objects.get(id=id)
    if request.method=="POST":
        form=Empinfo( request.POST,instance=employee)
        if form.is_valid():
            form.save(commit=True)
        return redirect("/")
    return render(request,'testapp/update.html',{'employee':employee})
    
