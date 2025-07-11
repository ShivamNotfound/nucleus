from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.models import User
from django.utils import timezone

def home(request):
    #shows all the tasks
    if request.method=='POST':
        task=Task.objects.get(id=request.POST['id'])
        task.status='completed'
        task.save()

    completed_today=Task.objects.filter(scheduled_date=timezone.now(),user=request.user,status='completed')
    today_tasks=Task.objects.filter(scheduled_date=timezone.now(),user=request.user,status='pending')
    unscheduled_tasks=Task.objects.filter(user=request.user,scheduled_date=None,status='pending')

    context={'today_tasks':today_tasks,'unscheduled_tasks':unscheduled_tasks,'completed_today':completed_today}
    return render(request,'home.html',context)

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

def deletetask(request,id):
    if request.method=='POST':
        task=Task.objects.get(id=id)
        task.delete()
        return redirect('home')
        
    return render(request,'base/deletetask.html')

def loginuser(request):
    if request.method=='POST':
        user=authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user:
            login(request,user)
            return redirect('home')
        else:
            return redirect("login")

    return render(request,'login.html')

def signupuser(request):
    if request.method=='POST':

        user=User.objects.create_user(username=request.POST['username'],password=request.POST['password'])
        login(request,user)
        return redirect("home")
    return render(request,'signup.html')

def logoutuser(request):

    logout(request)
    return redirect('login')