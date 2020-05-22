from django.shortcuts import render, redirect
from django.http import HttpResponse
from tasks.models import Task
import datetime
# Create your views here.
def home_view(request):
# Render the HTML template home.html
    task_list = Task.objects.all()
    context_dict = {'tasks' : task_list}
    return render(request, 'tasks/home.html', context_dict)

def add_view(request):
    return render(request, 'tasks/add.html')
def edit_view(request):
    task_list = Task.objects.all()
    context_dict = {'tasks' : task_list}
    return render(request, 'tasks/edit.html',context_dict)
def impressum_view(request):
    return render(request, 'tasks/impressum.html')
def add_todo(request):
    text = request.POST['task']
    date_tmp = request.POST['date'].split('/')
    date = datetime.date(int(date_tmp[2]), int(date_tmp[0]), int(date_tmp[1]))
    progress = int(request.POST['progress'])
    if progress >= 0 and progress <= 100:
        task = Task(task_text = text, task_progress = progress, task_deadline = date)
        task.save()
        return redirect('/')
    else:
        return redirect('/add/')    


