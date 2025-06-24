from django.shortcuts import render
from .models import Task
from .forms import TaskForm

def home(request):
    tasks=Task.objects.filter(user=request.user)
    return render(request,'home.html',{'tasks':tasks})

def addtask(request):
    form=TaskForm()
    return render(request,'base/createtask.html',{'form':form})