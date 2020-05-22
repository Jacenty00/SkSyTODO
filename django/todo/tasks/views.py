from django.shortcuts import render
from django.http import HttpResponse
from tasks.models import Task
# Create your views here.
def home(request):
# Render the HTML template home.html
    task_list = Task.objects.all()
    context_dict = {'tasks' : task_list}
    return render(request, 'tasks/home.html', context_dict)

def add(request):
    return render(request, 'tasks/add.html')
def edit(request):
    return render(request, 'tasks/edit.html')
def impressum(request):
    return render(request, 'tasks/impressum.html')        