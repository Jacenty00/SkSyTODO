from django.shortcuts import render
from django.http import HttpResponse
from tasks.models import Task
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
