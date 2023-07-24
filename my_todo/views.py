from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
# Create your views here.

def index(request):
    tasks = task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    mydict = {
        'tasks': tasks, 'form': form
    }
    return render(request, 'my_todo/index.html', mydict)


def updateTask(request, pk):
    mytasks = task.objects.get(id=pk)
    form = TaskForm(instance=mytasks)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance = mytasks)
        if form.is_valid():
            form.save()
            return redirect('/')
    mydict = {'form':form}    
    return render(request,'my_todo/update_task.html',mydict)


def deleteTask(request, pk):
    item = task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    mydict = {'item':item}
    return render(request, 'my_todo/delete.html',mydict)
     