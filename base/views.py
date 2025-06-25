from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm

def home(request):
    tasks=Task.objects.filter(user=request.user)
    return render(request,'home.html',{'tasks':tasks})

def addtask(request):
    if request.method=='POST':
        form=TaskForm(request.POST)
        f=form.save(commit=False)
        f.user=request.user
        f.save()
        return redirect('home')



    form=TaskForm()
    return render(request,'base/createtask.html',{'form':form})

def altertask(request,id):
    task=Task.objects.get(id=id)
    if request.method=='POST':
        form=TaskForm(request.POST,instance=task)
        f=form.save(commit=False)
        f.user=request.user
        f.save()
        return redirect('home')
    

    
    form=TaskForm(instance=task)
    return render(request,'base/createtask.html',{'form':form})
