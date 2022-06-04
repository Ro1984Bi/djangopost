import re
from django.shortcuts import redirect, render
from .models import Task

# Create your views here.
def list(request):
    tasks = Task.objects.all()
    print(tasks)
    return render(request, 'list.html', {"tasks": tasks})

def create_task(request):
 task = Task(title = request.POST['title'], description = request.POST['description'])
 task.save()
 return redirect('/tasks/')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('/tasks/')