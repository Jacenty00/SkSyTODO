from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
# Render the HTML template home.html
    return render(request, 'home.html')

def add(request):
    return render(request, 'add.html')
def edit(request):
    return render(request, 'edit.html')
def impressum(request):
    return render(request, 'impressum.html')        