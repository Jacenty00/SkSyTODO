from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Task
from datetime import datetime, date

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
    return render(request, 'tasks/edit.html', context_dict)

def impressum_view(request):
    return render(request, 'tasks/impressum.html')

def add_todo(request):
    if request.method == "POST":
        text = request.POST['task']
        date_tmp = request.POST['date'].split('/')
        deadline = date(int(date_tmp[2]), int(date_tmp[0]), int(date_tmp[1]))
        progress = int(request.POST['progress'])
        if (progress < 0 or progress > 100) or (deadline - date.today()).days < 0:
            return redirect('/add/')
        task = Task(task_text = text, task_progress = progress, task_deadline = deadline)
        task.save()
        return redirect('/')
    return Http404("No.")


def edit_todo(request):
    if request.method == "POST":
        id = request.POST['id']
        new_text = request.POST['text']
        new_progress = request.POST['progress']
        new_deadline = request.POST['deadline']
        try:

            to_edit = Task.objects.get(id = id)
            to_edit.task_text = new_text
            to_edit.task_progress = new_progress
            to_edit.task_deadline = datetime.strptime(new_deadline, "%m/%d/%Y")
            to_edit.save()

        except:
            raise Http404("Value not alowed")
        return redirect('/edit.html')
    return Http404("No task to edit")



def del_todo(request):
    if request.method == "POST":
        id = request.POST['id']
        try:
            to_delete = Task.objects.get(id = id)
            to_delete.delete()
        except Task.DoesNotExist:
            raise Http404("Task does not exist")
        return redirect('/')
    return Http404("No task to delete")
